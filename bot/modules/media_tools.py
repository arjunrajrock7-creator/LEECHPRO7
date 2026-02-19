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
        vt_ops = [
            ("Encode", "compress"), ("Watermark", "watermark"), ("Merge V+A", "merge_va"),
            ("Merge V+S", "merge_vs"), ("External Merge", "ext_merge"), ("Hardsub", "hardsub"),
            ("Extract", "extract"), ("Swap Audio", "swap_audio"), ("Remove Audio", "rem_audio"),
            ("Convert", "convert"), ("Concat", "concat"), ("Filters", "filters"),
            ("Intro", "intro"), ("Metadata", "metadata"), ("Attachments", "attach")
        ]
        for name, key in vt_ops:
            enabled = "✅" if user_dict.get(key) or (key == "compress" and user_dict.get("v_bitrate")) else "🔘"
            buttons.ibutton(f"{enabled} {name}", f"mediatool {key} {uid}")

        buttons.ibutton("✔ Confirm", f"mediatool confirm {uid}")
        buttons.ibutton("🔄 Reset", f"mediatool reset {uid}")
        buttons.ibutton("🔙 Back", f"userset {uid} leech")
        buttons.ibutton("🛑 Close", f"mediatool close")

        await editMessage(query.message, "☘️ <b>⚡𝗛𝗘𝗠𝗔𝗡𝗧𝗛⚡ PREMIUM VIDEO TOOLS</b> ☘️\n\n<i>Select tools to apply:</i>", buttons.build_menu(3))

    elif action == "close":
        await deleteMessage(query.message)

    elif action == "metadata":
        val = user_dict.get("lmeta", "Default")
        buttons = ButtonMaker()
        buttons.ibutton("General Tag", f"userset {uid} lmeta edit")
        buttons.ibutton("Video Tag", f"userset {uid} lmeta_video edit")
        buttons.ibutton("Audio Tag", f"userset {uid} lmeta_audio edit")
        buttons.ibutton("Subtitle Tag", f"userset {uid} lmeta_sub edit")

        rm_meta = "Enabled" if user_dict.get("remove_metadata", True) else "Disabled"
        buttons.ibutton(f"Remove Exists: {rm_meta}", f"userset {uid} remove_metadata")

        buttons.ibutton("Back", f"mediatool main {uid}")
        await editMessage(query.message, f"<b>Metadata Editor</b>\n\n<b>Current General:</b> <code>{val}</code>\n\nMetadata will be applied to all your leeched video files.", buttons.build_menu(2))

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
        buttons.ibutton("⚙️ Edit Sub Sync", f"userset {uid} v_subsync edit")
        buttons.ibutton("🔙 Back", f"mediatool main {uid}")
        await editMessage(query.message, f"<b>Subtitle Sync</b>\n\n<b>Delay:</b> <code>{val}s</code>\n\nPositive for delay, negative for advance.", buttons.build_menu(1))

    elif action == "intro":
        val = user_dict.get("v_intro", "None")
        buttons = ButtonMaker()
        buttons.ibutton("⚙️ Edit Intro Link", f"userset {uid} v_intro edit")
        buttons.ibutton("🔙 Back", f"mediatool main {uid}")
        await editMessage(query.message, f"<b>Intro Injection</b>\n\n<b>Current:</b> <code>{val}</code>\n\nPrepend an intro video to all your tasks.", buttons.build_menu(1))

    elif action == "attach":
        val = user_dict.get("v_attach", "None")
        buttons = ButtonMaker()
        buttons.ibutton("⚙️ Edit Attachments", f"userset {uid} v_attach edit")
        buttons.ibutton("🔙 Back", f"mediatool main {uid}")
        await editMessage(query.message, f"<b>MKV Attachments</b>\n\n<b>Current:</b> <code>{val}</code>\n\nFiles to be attached to MKV container (comma separated links).", buttons.build_menu(1))

    elif action in ["merge_va", "merge_vs", "ext_merge", "hardsub", "extract", "swap_audio", "rem_audio", "convert", "concat", "filters"]:
        # These will be implemented as toggles or simple input settings for now
        # To match the UI requirements, we show a basic edit prompt
        buttons = ButtonMaker()
        buttons.ibutton(f"⚙️ Configure {action.replace('_', ' ').title()}", f"userset {uid} v_{action} edit")
        buttons.ibutton("🔙 Back", f"mediatool main {uid}")
        await editMessage(query.message, f"<b>{action.replace('_', ' ').title()}</b>\n\nConfigure this tool for your tasks.", buttons.build_menu(1))

    elif action == "confirm":
        await query.answer("Tools Configured!", show_alert=True)
        await deleteMessage(query.message)

    elif action == "reset":
        # Clear all media tool related settings for user
        media_keys = ["v_bitrate", "v_watermark", "lmerge", "v_intro", "v_attach", "v_subsync", "audio_change", "default_audio"]
        for k in media_keys:
            if k in user_dict: del user_dict[k]
        await query.answer("All Video Tools Reset!", show_alert=True)
        await media_tools_callback(client, query) # Refresh main menu

bot.add_handler(CallbackQueryHandler(media_tools_callback, filters=regex("^mediatool")))
