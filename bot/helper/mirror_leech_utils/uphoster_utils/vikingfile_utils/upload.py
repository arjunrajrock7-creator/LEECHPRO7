from io import BufferedReader
from logging import getLogger
from os import path as ospath
from os import walk as oswalk
from pathlib import Path

import aiofiles
from aiofiles.os import path as aiopath
from aiohttp import ClientSession
from tenacity import (
    RetryError,
    retry,
    retry_if_exception_type,
    stop_after_attempt,
    wait_exponential,
)

from bot.core.config_manager import Config
from bot.helper.ext_utils.bot_utils import SetInterval, sync_to_async

LOGGER = getLogger(__name__)


class ProgressFileReader(BufferedReader):
    def __init__(self, filename, read_callback=None):
        super().__init__(open(filename, "rb"))
        self.__read_callback = read_callback
        self.length = Path(filename).stat().st_size

    def read(self, size=None):
        size = size or (self.length - self.tell())
        if self.__read_callback:
            self.__read_callback(self.tell())
        return super().read(size)

    def __len__(self):
        return self.length


class VikingFileUpload:
    def __init__(self, listener, path):
        self.listener = listener
        self._updater = None
        self._path = path
        self._is_errored = False
        self.api_url = "https://vikingfile.com/api/"
        self.__processed_bytes = 0
        self.last_uploaded = 0
        self.total_time = 0
        self.total_files = 0
        self.total_folders = 0
        self.is_uploading = True
        self.update_interval = 3

        from bot import user_data

        user_dict = user_data.get(self.listener.user_id, {})
        self.user_hash = user_dict.get("VIKINGFILE_USER") or Config.VIKINGFILE_USER

    @property
    def speed(self):
        try:
            return self.__processed_bytes / self.total_time
        except Exception:
            return 0

    @property
    def processed_bytes(self):
        return self.__processed_bytes

    def __progress_callback(self, current):
        chunk_size = current - self.last_uploaded
        self.last_uploaded = current
        self.__processed_bytes += chunk_size

    async def progress(self):
        self.total_time += self.update_interval

    async def _resp_handler(self, response):
        if response.get("error"):
            raise Exception(response.get("error"))
        return response

    async def _get_upload_url(self, size):
        payload = {"size": str(size)}
        async with ClientSession() as session:
            async with session.post(
                f"{self.api_url}get-upload-url", data=payload
            ) as resp:
                if resp.status != 200:
                    raise Exception(f"HTTP {resp.status}: {await resp.text()}")
                response = await resp.json()
                return await self._resp_handler(response)

    async def _upload_part(self, url, file_path, start, size):
        async def file_sender():
            remaining = size
            async with aiofiles.open(file_path, "rb") as afile:
                await afile.seek(start)
                while remaining > 0:
                    chunk = await afile.read(min(1024 * 1024, remaining))
                    if not chunk:
                        break
                    self.__processed_bytes += len(chunk)
                    remaining -= len(chunk)
                    yield chunk

        async with ClientSession() as session:
            async with session.put(url, data=file_sender()) as resp:
                if resp.status not in [200, 201, 204]:
                    raise Exception(f"HTTP {resp.status}: {await resp.text()}")
                etag = resp.headers.get("ETag") or resp.headers.get("ETAG")
                if not etag:
                    raise Exception("Missing ETag from VikingFile upload response.")
                return etag.strip('"')

    async def _complete_upload(self, key, upload_id, parts, name, path=""):
        data = [
            ("key", key),
            ("uploadId", upload_id),
            ("name", name),
            ("user", self.user_hash or ""),
        ]
        if path:
            data.append(("path", path))
        for index, part in enumerate(parts):
            data.append((f"parts[{index}][PartNumber]", str(part["PartNumber"])))
            data.append((f"parts[{index}][ETag]", part["ETag"]))
        async with ClientSession() as session:
            async with session.post(
                f"{self.api_url}complete-upload", data=data
            ) as resp:
                if resp.status != 200:
                    raise Exception(f"HTTP {resp.status}: {await resp.text()}")
                response = await resp.json()
                return await self._resp_handler(response)

    @retry(
        wait=wait_exponential(multiplier=2, min=4, max=8),
        stop=stop_after_attempt(3),
        retry=retry_if_exception_type(Exception),
    )
    async def _upload_file(self, path: str, upload_path: str = ""):
        file_name = ospath.basename(path).replace(" ", ".")
        file_size = Path(path).stat().st_size
        upload_info = await self._get_upload_url(file_size)
        key = upload_info["key"]
        upload_id = upload_info["uploadId"]
        part_size = int(upload_info["partSize"])
        urls = upload_info["urls"]

        parts = []
        for idx, url in enumerate(urls, start=1):
            start = (idx - 1) * part_size
            size = min(part_size, file_size - start)
            etag = await self._upload_part(url, path, start, size)
            parts.append({"PartNumber": idx, "ETag": etag})

        result = await self._complete_upload(
            key, upload_id, parts, file_name, path=upload_path
        )
        return result.get("url")

    async def _upload_dir(self, input_directory):
        folder_name = ospath.basename(input_directory.rstrip("/"))
        links = []

        for root, _, files in await sync_to_async(oswalk, input_directory):
            relative_dir = ospath.relpath(root, input_directory)
            upload_path = (
                folder_name
                if relative_dir == "."
                else f"{folder_name}/{relative_dir}"
            )
            for file in files:
                if self.listener.is_cancelled:
                    break
                file_path = ospath.join(root, file)
                link = await self._upload_file(file_path, upload_path)
                if link:
                    links.append(link)
                    self.total_files += 1

        if not links:
            raise Exception("No files uploaded from directory.")
        self.total_folders = 1
        return links[0]

    async def upload(self):
        try:
            LOGGER.info(f"VikingFile Uploading: {self._path}")
            self._updater = SetInterval(self.update_interval, self.progress)

            if not self.user_hash:
                raise Exception("VikingFile user hash not provided.")

            await self._upload_process()
        except Exception as err:
            if isinstance(err, RetryError):
                LOGGER.info(f"Total Attempts: {err.last_attempt.attempt_number}")
                err = err.last_attempt.exception()
            err = str(err).replace(">", "").replace("<", "")
            LOGGER.error(err)
            await self.listener.on_upload_error(err)
            self._is_errored = True
        finally:
            if self._updater:
                self._updater.cancel()
            if (
                self.listener.is_cancelled and not self._is_errored
            ) or self._is_errored:
                return

    async def _upload_process(self):
        link = ""
        if await aiopath.isfile(self._path):
            link = await self._upload_file(self._path)
            if link:
                mime_type = "File"
                self.total_files = 1
        else:
            link = await self._upload_dir(self._path)
            mime_type = "Folder"

        if not link:
            raise Exception("Failed to upload file to VikingFile.")

        await self.listener.on_upload_complete(
            link, self.total_files, self.total_folders, mime_type, ""
        )
