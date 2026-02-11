from pyrogram.handlers import MessageHandler, CallbackQueryHandler
from pyrogram.filters import command, regex
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from functools import partial

from bot import bot, LOGGER, user_data, config_dict
from bot.helper.telegram_helper.bot_commands import BotCommands
from bot.helper.telegram_helper.filters import CustomFilters
from bot.helper.telegram_helper.message_utils import sendMessage, editMessage, deleteMessage
from bot.helper.telegram_helper.button_build import ButtonMaker
from bot.helper.telegram_helper.callback_fix import callback_handler
from bot.helper.ext_utils.media_utils import MediaUtils
from bot.modules.users_settings import update_user_settings, get_user_settings

@callback_handler
async def media_tools_callback(client, query):
    user_id = query.from_user.id
    data = query.data.split()
    # data format: mediatool [action] [uid] [args...]
    action = data[1]
    uid = int(data[2]) if len(data) > 2 else user_id

    if user_id != uid:
        await query.answer("Not Yours!", show_alert=True)
        return

    user_dict = user_data.get(user_id, {})

    if action == "main":
        buttons = ButtonMaker()

        lmeta = "✅" if user_dict.get("lmeta") else "❌"
        buttons.ibutton(f"{lmeta} Metadata Editor", f"mediatool metadata {uid}")

        tracks = "✅" if user_dict.get("audio_change") or user_dict.get("default_audio") else "❌"
        buttons.ibutton(f"{tracks} Track Selection", f"mediatool tracks {uid}")

        compress = "✅" if user_dict.get("v_bitrate") else "❌"
        buttons.ibutton(f"{compress} Compressor", f"mediatool compress {uid}")

        merge = "✅" if user_dict.get("lmerge") else "❌"
        buttons.ibutton(f"{merge} Video + Video", f"mediatool merge {uid}")

        watermark = "✅" if user_dict.get("v_watermark") else "❌"
        buttons.ibutton(f"{watermark} Watermark", f"mediatool watermark {uid}")

        subsync = "✅" if user_dict.get("v_subsync") else "❌"
        buttons.ibutton(f"{subsync} Sub Sync", f"mediatool subsync {uid}")

        buttons.ibutton("Back to Settings", f"userset {uid} leech")
        buttons.ibutton("Close", f"mediatool close")
        await editMessage(query.message, "☘️ <b>⚡𝗛𝗘𝗠𝗔𝗡𝗧𝗛⚡ VIDEO TOOLS</b> ☘️\n\n<i>Configure your global video processing settings below:</i>", buttons.build_menu(2))

    elif action == "close":
        await deleteMessage(query.message)

    elif action == "metadata":
        val = user_dict.get("lmeta", "Default")
        buttons = ButtonMaker()
        buttons.ibutton("Edit Metadata", f"userset {uid} lmeta edit")
        buttons.ibutton("Back", f"mediatool main {uid}")
        await editMessage(query.message, f"<b>Metadata Editor</b>\n\n<b>Current:</b> <code>{val}</code>\n\nMetadata will be applied to all your leeched video files.", buttons.build_menu(1))

    elif action == "tracks":
        ac = user_dict.get("audio_change", "Default")
        da = user_dict.get("default_audio", "0")
        buttons = ButtonMaker()
        buttons.ibutton("Edit Audio Tracks", f"userset {uid} audio_change edit")
        buttons.ibutton("Edit Default Audio", f"userset {uid} default_audio edit")
        buttons.ibutton("Back", f"mediatool main {uid}")
        await editMessage(query.message, f"<b>Track Selection</b>\n\n<b>Audio Order:</b> <code>{ac}</code>\n<b>Default Audio:</b> <code>{da}</code>\n\nUse stream indices separated by commas.", buttons.build_menu(1))

    elif action == "compress":
        bitrate = user_dict.get("v_bitrate", "Original")
        buttons = ButtonMaker()
        buttons.ibutton("Edit Bitrate", f"userset {uid} v_bitrate edit")
        buttons.ibutton("Back", f"mediatool main {uid}")
        await editMessage(query.message, f"<b>Video Compressor</b>\n\n<b>Bitrate:</b> <code>{bitrate}</code>\n\nSet video bitrate (e.g., 2M, 800k) for compression.", buttons.build_menu(1))

    elif action == "merge":
        mode = "Enabled" if user_dict.get("lmerge") else "Disabled"
        buttons = ButtonMaker()
        buttons.ibutton("Toggle Merge", f"userset {uid} lmerge")
        buttons.ibutton("Back", f"mediatool main {uid}")
        await editMessage(query.message, f"<b>Video Merger</b>\n\n<b>Status:</b> <code>{mode}</code>\n\nAutomatically merges all extracted videos in a task.", buttons.build_menu(1))

    elif action == "watermark":
        val = user_dict.get("v_watermark", "None")
        buttons = ButtonMaker()
        buttons.ibutton("Edit Watermark", f"userset {uid} v_watermark edit")
        buttons.ibutton("Back", f"mediatool main {uid}")
        await editMessage(query.message, f"<b>Video Watermark</b>\n\n<b>Value:</b> <code>{val}</code>\n\nSet image link or text for watermark.", buttons.build_menu(1))

    elif action == "subsync":
        val = user_dict.get("v_subsync", "0")
        buttons = ButtonMaker()
        buttons.ibutton("Edit Sub Sync", f"userset {uid} v_subsync edit")
        buttons.ibutton("Back", f"mediatool main {uid}")
        await editMessage(query.message, f"<b>Subtitle Sync</b>\n\n<b>Delay:</b> <code>{val}s</code>\n\nPositive for delay, negative for advance.", buttons.build_menu(1))

bot.add_handler(CallbackQueryHandler(media_tools_callback, filters=regex("^mediatool")))
