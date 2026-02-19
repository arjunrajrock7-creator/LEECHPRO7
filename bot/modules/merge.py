from pyrogram.handlers import MessageHandler
from pyrogram.filters import command, reply, user
from asyncio import Event

from bot import bot, DOWNLOAD_DIR, LOGGER, user_data
from bot.helper.telegram_helper.bot_commands import BotCommands
from bot.helper.telegram_helper.filters import CustomFilters
from bot.helper.telegram_helper.message_utils import sendMessage, deleteMessage
from bot.helper.ext_utils.bot_utils import new_task, arg_parser
from bot.helper.listeners.tasks_listener import MirrorLeechListener
from bot.helper.mirror_utils.download_utils.telegram_download import TelegramDownloadHelper

merge_dict = {}

@new_task
async def merge_files(client, message):
    user_id = message.from_user.id
    input_list = message.text.split(" ")
    arg_base = {"-i": "0", "-n": ""}
    args = arg_parser(input_list[1:], arg_base)

    count = int(args["-i"]) if args["-i"].isdigit() else 0
    name = args["-n"]

    if count < 2:
        return await sendMessage(message, "Use <code>/merge2 -i [count] -n [filename]</code> to merge files. Minimum count is 2.")

    if user_id in merge_dict:
        return await sendMessage(message, "You already have a merge task in progress. Use /cancelmerge to stop.")

    merge_dict[user_id] = {"count": count, "name": name, "messages": []}

    # Check if replied to a message
    if message.reply_to_message:
        merge_dict[user_id]["messages"].append(message.reply_to_message)
        if len(merge_dict[user_id]["messages"]) == count:
            await start_merge(client, user_id, message)
            return

    await sendMessage(message, f"Merge task started ({len(merge_dict[user_id]['messages'])}/{count}). Reply to other files with any text to collect them.")

@new_task
async def cancel_merge(client, message):
    user_id = message.from_user.id
    if user_id in merge_dict:
        del merge_dict[user_id]
        await sendMessage(message, "Merge task cancelled.")
    else:
        await sendMessage(message, "No active merge task.")

async def collect_files(client, message):
    user_id = message.from_user.id
    if user_id not in merge_dict:
        return

    if not message.reply_to_message:
        return

    data = merge_dict[user_id]
    replied_msg = message.reply_to_message

    if replied_msg in data["messages"]:
        return await sendMessage(message, "File already collected.")

    data["messages"].append(replied_msg)
    await deleteMessage(message)

    if len(data["messages"]) < data["count"]:
        await sendMessage(replied_msg, f"File {len(data['messages'])}/{data['count']} collected.")
    else:
        await start_merge(client, user_id, replied_msg)

async def start_merge(client, user_id, message):
    data = merge_dict.pop(user_id)
    count = data["count"]
    name = data["name"]
    messages = data["messages"]

    listener = MirrorLeechListener(
        message,
        isLeech=True,
        tag=message.from_user.mention,
        join=True
    )

    path = f"{DOWNLOAD_DIR}{listener.uid}/"

    await sendMessage(message, f"Collected {count} files. Starting download...")

    # We download them one by one into the same folder
    for msg in messages:
        tg_download = TelegramDownloadHelper(listener)
        # We need to manually download here or adapt TelegramDownloadHelper
        # to not call onDownloadComplete until all are done.
        # But MirrorLeechListener.onDownloadComplete has sameDir logic!

    # Actually, let's use a simpler way: download them and then call join_files.
    # Since I'm an expert, I'll do it right.

    # We'll use the sameDir logic of MirrorLeechListener.
    sameDir = {"total": count, "tasks": set(), "name": "MergeFolder"}

    for i, msg in enumerate(messages):
        # Create a dummy message for each part if needed,
        # but here we can just trigger multiple downloads with same sameDir.
        l = MirrorLeechListener(
            msg,
            isLeech=True,
            tag=msg.from_user.mention,
            join=True,
            sameDir=sameDir
        )
        sameDir["tasks"].add(l.uid)
        tg_download = TelegramDownloadHelper(l)
        await tg_download.add_download(msg, f"{DOWNLOAD_DIR}{l.uid}/MergeFolder/", f"part_{i}_{name}" if name else None)

bot.add_handler(MessageHandler(merge_files, filters=command(BotCommands.MergeCommand) & CustomFilters.authorized))
bot.add_handler(MessageHandler(cancel_merge, filters=command("cancelmerge") & CustomFilters.authorized))
bot.add_handler(MessageHandler(collect_files, filters=~command(BotCommands.MergeCommand) & CustomFilters.authorized & reply))
