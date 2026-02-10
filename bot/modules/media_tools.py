from pyrogram.handlers import MessageHandler, CallbackQueryHandler
from pyrogram.filters import command, regex
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from bot import bot, LOGGER, user_data, config_dict
from bot.helper.telegram_helper.bot_commands import BotCommands
from bot.helper.telegram_helper.filters import CustomFilters
from bot.helper.telegram_helper.message_utils import sendMessage, editMessage, deleteMessage
from bot.helper.telegram_helper.button_build import ButtonMaker
from bot.helper.telegram_helper.callback_fix import callback_handler
from bot.helper.ext_utils.media_utils import MediaUtils

@callback_handler
async def media_tools_callback(client, query):
    user_id = query.from_user.id
    data = query.data.split()
    # data format: mediatool [action] [uid] [args...]
    action = data[1]

    if action == "main":
        # show main menu of media tools
        buttons = ButtonMaker()
        buttons.ibutton("Metadata Editor", f"mediatool metadata {data[2]}")
        buttons.ibutton("Track Selection", f"mediatool tracks {data[2]}")
        buttons.ibutton("Compressor", f"mediatool compress {data[2]}")
        buttons.ibutton("Close", f"mediatool close")
        await editMessage(query.message, "<b>FFmpeg Media Tools Menu</b>", buttons.build_menu(2))
    elif action == "close":
        await deleteMessage(query.message)
    elif action == "metadata":
        # metadata editor menu
        buttons = ButtonMaker()
        buttons.ibutton("Back", f"mediatool main {data[2]}")
        await editMessage(query.message, "<b>Metadata Editor - Under Development</b>", buttons.build_menu(1))

# Register handlers (example)
# bot.add_handler(CallbackQueryHandler(media_tools_callback, filters=regex("^mediatool")))
