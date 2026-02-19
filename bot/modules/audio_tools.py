from pyrogram.handlers import MessageHandler, CallbackQueryHandler
from pyrogram.filters import command, regex
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import os
import asyncio

from bot import bot, DOWNLOAD_DIR, LOGGER
from bot.helper.telegram_helper.bot_commands import BotCommands
from bot.helper.telegram_helper.filters import CustomFilters
from bot.helper.telegram_helper.message_utils import sendMessage, editMessage, deleteMessage
from bot.helper.telegram_helper.button_build import ButtonMaker
from bot.helper.ext_utils.bot_utils import new_task, cmd_exec, sync_to_async
from bot.helper.ext_utils.media_utils import MediaUtils
from bot.helper.listeners.tasks_listener import MirrorLeechListener
from bot.helper.mirror_utils.download_utils.telegram_download import TelegramDownloadHelper

audio_state = {}

@new_task
async def audio_tools(client, message):
    rply = message.reply_to_message
    if not rply or not (rply.document or rply.video):
        return await sendMessage(message, "Reply to a video or document file.")

    msg = await sendMessage(message, "<i>Downloading file to analyze streams...</i>")

    # We need to download at least enough to get streams.
    # For many formats, we need the whole thing if it's not streamed.
    # To be safe and meet the requirement "file download after show all audios", we download it.

    listener = MirrorLeechListener(message, isLeech=True, tag=message.from_user.mention)
    path = f"{DOWNLOAD_DIR}audio_{message.id}/"
    os.makedirs(path, exist_ok=True)

    # We'll use a simplified download here
    file_path = await client.download_media(rply, file_name=path)

    streams = await MediaUtils.get_streams(file_path)
    audio_streams = [s for s in streams if s.get("codec_type") == "audio"]

    if not audio_streams:
        await deleteMessage(msg)
        os.remove(file_path)
        return await sendMessage(message, "No audio streams found in this file.")

    audio_state[message.id] = {
        "path": file_path,
        "streams": audio_streams,
        "selected": [s.get("index") for s in audio_streams],
        "listener": listener
    }

    await show_audio_selection(msg, message.id)

async def show_audio_selection(message, state_id):
    data = audio_state[state_id]
    buttons = ButtonMaker()
    for s in data["streams"]:
        idx = s.get("index")
        lang = s.get("tags", {}).get("language", "und")
        codec = s.get("codec_name", "unknown")
        selected = "✅" if idx in data["selected"] else "❌"
        buttons.ibutton(f"{selected} Stream {idx} ({lang} - {codec})", f"audiostream {state_id} {idx}")

    buttons.ibutton("DONE", f"audiostream {state_id} done")
    buttons.ibutton("CANCEL", f"audiostream {state_id} cancel")

    await editMessage(message, "Select the audio streams you want to KEEP:", buttons.build_menu(1))

@CallbackQueryHandler
@new_task
async def audio_callback(client, query):
    data = query.data.split()
    state_id = int(data[1])
    action = data[2]

    if state_id not in audio_state:
        return await query.answer("Session expired.", show_alert=True)

    state = audio_state[state_id]

    if action == "done":
        if not state["selected"]:
            return await query.answer("Select at least one stream!", show_alert=True)
        await query.answer("Processing...")
        await process_audio(query.message, state_id)
    elif action == "cancel":
        file_path = state["path"]
        if os.path.exists(file_path):
            os.remove(file_path)
        del audio_state[state_id]
        await deleteMessage(query.message)
    else:
        stream_idx = int(action)
        if stream_idx in state["selected"]:
            state["selected"].remove(stream_idx)
        else:
            state["selected"].append(stream_idx)
        await show_audio_selection(query.message, state_id)

async def process_audio(message, state_id):
    state = audio_state.pop(state_id)
    input_path = state["path"]
    selected = state["selected"]
    listener = state["listener"]

    output_path = f"{input_path}.processed.mkv"

    # Construct ffmpeg command
    cmd = ["ffmpeg", "-hide_banner", "-loglevel", "error", "-i", input_path, "-map", "0:v:0"]
    # Map selected audio streams
    # ffmpeg indices for mapping are often different from absolute indices if we use 0:a:N
    # But here we have absolute indices from ffprobe.
    for idx in selected:
        cmd.extend(["-map", f"0:{idx}"])

    # Map all subtitles as well? Requirement says "remove unselected audios", doesn't mention subtitles.
    # To be safe, keep subtitles.
    cmd.extend(["-map", "0:s?", "-c", "copy", output_path, "-y"])

    await editMessage(message, "<i>Processing video with selected audio streams...</i>")
    stdout, stderr, rc = await cmd_exec(cmd)

    if rc != 0:
        await editMessage(message, f"Error processing audio: {stderr}")
        if os.path.exists(input_path): os.remove(input_path)
        return

    await editMessage(message, "<i>Upload started...</i>")
    # Trigger upload via listener
    # We need to move the output to the listener's directory
    final_dir = f"{DOWNLOAD_DIR}{listener.uid}/"
    os.makedirs(final_dir, exist_ok=True)
    final_path = os.path.join(final_dir, os.path.basename(input_path))
    os.rename(output_path, final_path)

    if os.path.exists(input_path): os.remove(input_path)

    # Manually trigger the upload complete cycle
    # Or better, use listener.onDownloadComplete() if we set it up correctly.
    # But we already have the file.
    await listener.onDownloadComplete()
    await deleteMessage(message)

bot.add_handler(MessageHandler(audio_tools, filters=command(BotCommands.AudioCommand) & CustomFilters.authorized))
bot.add_handler(CallbackQueryHandler(audio_callback, filters=regex("^audiostream")))
