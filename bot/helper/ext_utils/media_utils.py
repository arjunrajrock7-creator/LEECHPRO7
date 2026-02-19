import os
import re
import json
import shlex
import asyncio
import multiprocessing
from bot import LOGGER, bot_cache, config_dict
from bot.helper.ext_utils.bot_utils import cmd_exec

class MediaUtils:
    @staticmethod
    def get_optimal_threads():
        if threads := config_dict.get("FFMPEG_THREADS"):
            return str(threads)
        return str(multiprocessing.cpu_count())

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
        try:
            return json.loads(stdout).get("streams", [])
        except:
            return []

    @staticmethod
    async def strip_metadata(path, out_path):
        threads = MediaUtils.get_optimal_threads()
        cmd = [
            "ffmpeg",
            "-hide_banner",
            "-loglevel",
            "error",
            "-hwaccel", "auto",
            "-i", path,
            "-map_metadata", "-1",
            "-c", "copy",
            "-threads", threads,
            out_path,
            "-y"
        ]
        _, stderr, rc = await cmd_exec(cmd)
        return rc == 0, stderr

    @staticmethod
    async def process_custom_ffmpeg(path, cmd_list, listener):
        from bot.helper.ext_utils.leech_utils import get_document_type

        files = []
        if os.path.isfile(path):
            files.append(path)
        else:
            for root, _, fs in os.walk(path):
                for f in fs:
                    files.append(os.path.join(root, f))

        for f_path in files:
            is_video, is_audio, _ = await get_document_type(f_path)
            base_name, extension = os.path.splitext(f_path)
            ext = extension[1:] if extension.startswith('.') else extension

            curr_f_path = f_path
            for cmd_str in cmd_list:
                should_del = "-del" in cmd_str
                pure_cmd = cmd_str.replace("-del", "").strip()

                parts = shlex.split(pure_cmd)

                # Filter check
                skip = False
                if "-i" in parts:
                    idx = parts.index("-i")
                    if idx + 1 < len(parts):
                        inp = parts[idx+1]
                        if inp.startswith("mltb."):
                            p_ext = inp.split(".", 1)[1]
                            if p_ext == "video" and not is_video: skip = True
                            elif p_ext == "audio" and not is_audio: skip = True
                            elif p_ext not in ["video", "audio"] and p_ext != ext: skip = True
                if skip: continue

                # Replacement
                new_parts = []
                for p in parts:
                    if p.startswith("mltb."):
                        p_ext = p.split(".", 1)[1]
                        if p_ext == "video" or p_ext == "audio":
                            new_parts.append(curr_f_path)
                        else:
                            new_parts.append(f"{base_name}.{p_ext}")
                    elif p == "mltb":
                        new_parts.append(curr_f_path)
                    else:
                        new_parts.append(p)

                output_path = None
                for part in reversed(new_parts):
                    if not part.startswith("-"):
                        output_path = part
                        break

                full_cmd = ["ffmpeg", "-hide_banner", "-loglevel", "error"] + new_parts
                if "-y" not in full_cmd:
                    full_cmd.append("-y")

                success, err = await listener.run_ffmpeg_with_watchdog(full_cmd)
                if success:
                    if should_del and os.path.exists(curr_f_path) and output_path and os.path.abspath(curr_f_path) != os.path.abspath(output_path):
                        os.remove(curr_f_path)
                    if output_path and os.path.exists(output_path):
                        curr_f_path = output_path
                        _, extension = os.path.splitext(curr_f_path)
                        ext = extension[1:] if extension.startswith('.') else extension
                else:
                    LOGGER.error(f"Custom FFmpeg failed for {curr_f_path}: {err}")

    @staticmethod
    async def attachment_manager(path, out_path, attach_files=None, remove_attachments=False):
        cmd = ["mkvmerge", "-o", out_path]
        if remove_attachments:
            cmd.append("--no-attachments")
        cmd.append(path)
        if attach_files:
            for file in attach_files:
                if os.path.exists(file):
                    cmd.extend(["--attach-file", file])
        _, stderr, rc = await cmd_exec(cmd)
        return rc == 0, stderr

    @staticmethod
    async def inject_intro_video(path, intro_path, out_path):
        threads = MediaUtils.get_optimal_threads()
        cmd = [
            "ffmpeg",
            "-hide_banner",
            "-loglevel",
            "error",
            "-hwaccel", "auto",
            "-i", intro_path,
            "-i", path,
            "-filter_complex", "[0:v][0:a][1:v][1:a]concat=n=2:v=1:a=1[v][a]",
            "-map", "[v]",
            "-map", "[a]",
            "-c:v", "libx264",
            "-preset", "ultrafast",
            "-threads", threads,
            out_path,
            "-y"
        ]
        _, stderr, rc = await cmd_exec(cmd)
        return rc == 0, stderr

    @staticmethod
    async def merge_videos(video_list, out_path, user_ffmpeg_cmds=None):
        """
        Optimized video merging using concat demuxer if possible,
        or transcoding with ultrafast preset if necessary/requested.
        """
        threads = MediaUtils.get_optimal_threads()
        list_path = f"{out_path}.txt"
        with open(list_path, "w", encoding='utf-8') as f:
            for video in video_list:
                f.write(f"file '{os.path.abspath(video)}'\n")

        # Default to stream copy for speed and quality preservation
        cmd = [
            "ffmpeg",
            "-hide_banner",
            "-loglevel",
            "error",
            "-hwaccel", "auto",
            "-f", "concat",
            "-safe", "0",
            "-i", list_path,
            "-c", "copy",
            "-threads", threads,
            out_path,
            "-y"
        ]

        # If user has custom FFmpeg commands, we might need to transcode
        if user_ffmpeg_cmds:
            # Re-build command for transcoding if user specifies encoding params
            cmd = [
                "ffmpeg",
                "-hide_banner",
                "-loglevel",
                "error",
                "-f", "concat",
                "-safe", "0",
                "-i", list_path
            ]
            cmd.extend(user_ffmpeg_cmds.split())
            cmd.extend(["-threads", threads, out_path, "-y"])

        _, stderr, rc = await cmd_exec(cmd)

        # If concat copy fails, try transcoding with ultrafast preset as fallback
        if rc != 0 and not user_ffmpeg_cmds:
            LOGGER.warning(f"Concat copy failed, falling back to transcoding for merge: {stderr}")
            cmd = [
                "ffmpeg",
                "-hide_banner",
                "-loglevel",
                "error",
                "-f", "concat",
                "-safe", "0",
                "-i", list_path,
                "-c:v", "libx264",
                "-preset", "ultrafast",
                "-c:a", "aac",
                "-threads", threads,
                out_path,
                "-y"
            ]
            _, stderr, rc = await cmd_exec(cmd)

        if os.path.exists(list_path):
            os.remove(list_path)
        return rc == 0, stderr

    @staticmethod
    async def add_watermark(path, watermark_path, out_path, position="main_w-overlay_w-10:main_h-overlay_h-10"):
        threads = MediaUtils.get_optimal_threads()
        cmd = [
            "ffmpeg",
            "-hide_banner",
            "-loglevel",
            "error",
            "-hwaccel", "auto",
            "-i", path,
            "-i", watermark_path,
            "-filter_complex", f"overlay={position}",
            "-c:v", "libx264",
            "-preset", "ultrafast",
            "-threads", threads,
            "-c:a", "copy",
            out_path,
            "-y"
        ]
        _, stderr, rc = await cmd_exec(cmd)
        return rc == 0, stderr

    @staticmethod
    async def sync_subtitles(path, sub_path, out_path, delay=0):
        threads = MediaUtils.get_optimal_threads()
        cmd = [
            "ffmpeg",
            "-hide_banner",
            "-loglevel",
            "error",
            "-hwaccel", "auto",
            "-i", path,
            "-itsoffset", str(delay),
            "-i", sub_path,
            "-map", "0",
            "-map", "1",
            "-c", "copy",
            "-threads", threads,
            out_path,
            "-y"
        ]
        _, stderr, rc = await cmd_exec(cmd)
        return rc == 0, stderr

    @staticmethod
    async def track_selection(path, out_path, audio_tracks=None, sub_tracks=None, default_audio=None, default_sub=None):
        threads = MediaUtils.get_optimal_threads()
        cmd = ["ffmpeg", "-hide_banner", "-loglevel", "error", "-hwaccel", "auto", "-i", path]
        cmd.extend(["-map", "0:v:0"])
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

        cmd.extend(["-c", "copy", "-threads", threads])

        if default_audio is not None:
            cmd.extend([f"-disposition:a:{default_audio}", "default"])
        if default_sub is not None:
            cmd.extend([f"-disposition:s:{default_sub}", "default"])

        cmd.extend([out_path, "-y"])
        _, stderr, rc = await cmd_exec(cmd)
        return rc == 0, stderr

    @staticmethod
    async def add_intro_subtrack(path, sub_path, out_path):
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
        threads = MediaUtils.get_optimal_threads()
        cmd = ["ffmpeg", "-hide_banner", "-loglevel", "error", "-hwaccel", "auto", "-i", path]
        for key, value in metadata.items():
            cmd.extend(["-metadata", f"{key}={value}"])
        cmd.extend(["-c", "copy", "-threads", threads, out_path, "-y"])
        _, stderr, rc = await cmd_exec(cmd)
        return rc == 0, stderr

    @staticmethod
    async def compress_video(path, out_path, bitrate=None, user_ffmpeg_cmds=None):
        """
        Aggressive yet high-quality video compression using libx265 (if possible) or libx264.
        Default to libx264 with ultrafast preset for maximum speed as requested.
        """
        threads = MediaUtils.get_optimal_threads()
        cmd = [
            "ffmpeg",
            "-hide_banner",
            "-loglevel",
            "error",
            "-hwaccel", "auto",
            "-i", path
        ]

        if user_ffmpeg_cmds:
            cmd.extend(user_ffmpeg_cmds.split())
        else:
            if not bitrate:
                bitrate = "1M"
            cmd.extend([
                "-c:v", "libx264",
                "-b:v", bitrate,
                "-preset", "ultrafast",
                "-c:a", "aac",
                "-b:a", "128k"
            ])

        cmd.extend(["-threads", threads, out_path, "-y"])
        _, stderr, rc = await cmd_exec(cmd)
        return rc == 0, stderr

    @staticmethod
    async def apply_custom_ffmpeg(path, out_path, user_ffmpeg_cmds):
        threads = MediaUtils.get_optimal_threads()
        cmd = [
            "ffmpeg",
            "-hide_banner",
            "-loglevel",
            "error",
            "-hwaccel", "auto",
            "-i", path
        ]
        cmd.extend(user_ffmpeg_cmds.split())
        cmd.extend(["-threads", threads, out_path, "-y"])
        _, stderr, rc = await cmd_exec(cmd)
        return rc == 0, stderr

    @staticmethod
    async def take_sample(path, out_path, duration=30):
        threads = MediaUtils.get_optimal_threads()
        cmd = [
            "ffmpeg",
            "-hide_banner",
            "-loglevel",
            "error",
            "-hwaccel", "auto",
            "-ss", "00:00:00",
            "-i", path,
            "-t", str(duration),
            "-c", "copy",
            "-threads", threads,
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
