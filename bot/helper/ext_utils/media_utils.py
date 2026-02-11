import os
import asyncio
from bot import LOGGER, bot_cache
from bot.helper.ext_utils.bot_utils import cmd_exec

class MediaUtils:
    @staticmethod
    async def get_streams(path):
        cmd = [
            "ffprobe",
            "-hide_banner",
            "-loglevel",
            "error",
            "-print_format",
            "json",
            "-show_streams",
            path
        ]
        stdout, stderr, rc = await cmd_exec(cmd)
        if rc != 0:
            LOGGER.error(f"FFprobe failed for {path}: {stderr}")
            return []
        import json
        return json.loads(stdout).get("streams", [])

    @staticmethod
    async def strip_metadata(path, out_path):
        cmd = [
            "ffmpeg",
            "-hide_banner",
            "-loglevel",
            "error",
            "-i", path,
            "-map_metadata", "-1",
            "-c", "copy",
            out_path,
            "-y"
        ]
        _, stderr, rc = await cmd_exec(cmd)
        return rc == 0, stderr

    @staticmethod
    async def merge_videos(video_list, out_path):
        # uses concat demuxer
        list_path = f"{out_path}.txt"
        with open(list_path, "w") as f:
            for video in video_list:
                f.write(f"file '{video}'\n")

        cmd = [
            "ffmpeg",
            "-hide_banner",
            "-loglevel",
            "error",
            "-f", "concat",
            "-safe", "0",
            "-i", list_path,
            "-c", "copy",
            out_path,
            "-y"
        ]
        _, stderr, rc = await cmd_exec(cmd)
        if os.path.exists(list_path):
            os.remove(list_path)
        return rc == 0, stderr

    @staticmethod
    async def add_watermark(path, watermark_path, out_path, position="main_w-overlay_w-10:main_h-overlay_h-10"):
        cmd = [
            "ffmpeg",
            "-hide_banner",
            "-loglevel",
            "error",
            "-i", path,
            "-i", watermark_path,
            "-filter_complex", f"overlay={position}",
            "-c:a", "copy",
            out_path,
            "-y"
        ]
        _, stderr, rc = await cmd_exec(cmd)
        return rc == 0, stderr

    @staticmethod
    async def sync_subtitles(path, sub_path, out_path, delay=0):
        # delay in seconds
        cmd = [
            "ffmpeg",
            "-hide_banner",
            "-loglevel",
            "error",
            "-i", path,
            "-itsoffset", str(delay),
            "-i", sub_path,
            "-map", "0",
            "-map", "1",
            "-c", "copy",
            out_path,
            "-y"
        ]
        _, stderr, rc = await cmd_exec(cmd)
        return rc == 0, stderr

    @staticmethod
    async def track_selection(path, out_path, audio_tracks=None, sub_tracks=None, default_audio=None, default_sub=None):
        # audio_tracks and sub_tracks are lists of stream indices
        cmd = ["ffmpeg", "-hide_banner", "-loglevel", "error", "-i", path]
        cmd.extend(["-map", "0:v:0"]) # Always keep first video track
        if audio_tracks:
            for track in audio_tracks:
                cmd.extend(["-map", f"0:a:{track}"])
        else:
            cmd.extend(["-map", "0:a?"])

        if sub_tracks:
            for track in sub_tracks:
                cmd.extend(["-map", f"0:s:{track}"])
        else:
            cmd.extend(["-map", "0:s?"])

        cmd.extend(["-c", "copy"])

        if default_audio is not None:
            cmd.extend([f"-disposition:a:{default_audio}", "default"])
        if default_sub is not None:
            cmd.extend([f"-disposition:s:{default_sub}", "default"])

        cmd.extend([out_path, "-y"])
        _, stderr, rc = await cmd_exec(cmd)
        return rc == 0, stderr

    @staticmethod
    async def add_intro_subtrack(path, sub_path, out_path):
        # basic mkvmerge intro sub
        cmd = [
            "mkvmerge",
            "-o", out_path,
            path,
            "--track-name", "0:Intro",
            sub_path
        ]
        _, stderr, rc = await cmd_exec(cmd)
        return rc == 0, stderr

    @staticmethod
    async def edit_metadata(path, out_path, metadata):
        # metadata is a dict like {'title': '...', 'artist': '...'}
        cmd = ["ffmpeg", "-hide_banner", "-loglevel", "error", "-i", path]
        for key, value in metadata.items():
            cmd.extend(["-metadata", f"{key}={value}"])
        cmd.extend(["-c", "copy", out_path, "-y"])
        _, stderr, rc = await cmd_exec(cmd)
        return rc == 0, stderr

    @staticmethod
    async def compress_video(path, out_path, bitrate="1M"):
        cmd = [
            "ffmpeg",
            "-hide_banner",
            "-loglevel",
            "error",
            "-i", path,
            "-b:v", bitrate,
            "-c:a", "copy",
            out_path,
            "-y"
        ]
        _, stderr, rc = await cmd_exec(cmd)
        return rc == 0, stderr

    @staticmethod
    async def take_sample(path, out_path, duration=30):
        cmd = [
            "ffmpeg",
            "-hide_banner",
            "-loglevel",
            "error",
            "-ss", "00:00:00",
            "-i", path,
            "-t", str(duration),
            "-c", "copy",
            out_path,
            "-y"
        ]
        _, stderr, rc = await cmd_exec(cmd)
        return rc == 0, stderr

    @staticmethod
    async def extract_thumbnail(path, out_path, timestamp="00:00:05"):
        cmd = [
            "ffmpeg",
            "-hide_banner",
            "-loglevel",
            "error",
            "-ss", timestamp,
            "-i", path,
            "-vframes", "1",
            out_path,
            "-y"
        ]
        _, stderr, rc = await cmd_exec(cmd)
        return rc == 0, stderr
