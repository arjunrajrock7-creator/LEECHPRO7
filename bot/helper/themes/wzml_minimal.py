#!/usr/bin/env python3
class WZMLStyle:
    # ----------------------
    # async def start(client, message) ---> __main__.py
    ST_BN1_NAME = "Repo"
    ST_BN1_URL = "https://github.com/arjunrajrock7-creator/LEECHPRO7"
    ST_BN2_NAME = "Updates"
    ST_BN2_URL = "https://t.me/ALONEKINGSTAR77"
    ST_MSG = """<i>This bot can mirror all your links|files|torrents to Google Drive or any rclone cloud or to telegram or to ddl servers.</i>
<b>Type {help_command} to get a list of available commands</b>"""
    ST_BOTPM = """<i>Now, This bot will send all your files and links here. Start Using ...</i>"""
    ST_UNAUTH = """<i>You Are not authorized user! Deploy your own ⚡𝗛𝗘𝗠𝗔𝗡𝗧𝗛⚡ Mirror-Leech bot</i>"""
    OWN_TOKEN_GENERATE = (
        """<b>Temporary Token is not yours!</b>\n\n<i>Kindly generate your own.</i>"""
    )
    USED_TOKEN = (
        """<b>Temporary Token already used!</b>\n\n<i>Kindly generate a new one.</i>"""
    )
    LOGGED_PASSWORD = """<b>Bot Already Logged In via Password</b>\n\n<i>No Need to Accept Temp Tokens.</i>"""
    ACTIVATE_BUTTON = "Activate Temporary Token"
    TOKEN_MSG = """<b><u>Generated Temporary Login Token!</u></b>
<b>Temp Token:</b> <code>{token}</code>
<b>Validity:</b> {validity}"""
    # ---------------------
    # async def token_callback(_, query): ---> __main__.py
    ACTIVATED = "✅️ Activated ✅"
    # ---------------------
    # async def login(_, message): --> __main__.py
    LOGGED_IN = "<b>Already Bot Login In!</b>"
    INVALID_PASS = "<b>Invalid Password!</b>\n\nKindly put the correct Password ."
    PASS_LOGGED = "<b>Bot Permanent Login Successfully!</b>"
    LOGIN_USED = "<b>Bot Login Usage :</b>\n\n<code>/cmd [password]</code>"
    # ---------------------
    # async def log(_, message): ---> __main__.py
    LOG_DISPLAY_BT = "📑 Log Display"
    WEB_PASTE_BT = "📨 Web Paste (SB)"
    # ---------------------
    # async def bot_help(client, message): ---> __main__.py
    BASIC_BT = "Basic"
    USER_BT = "Users"
    MICS_BT = "Mics"
    O_S_BT = "Owner & Sudos"
    CLOSE_BT = "Close"
    HELP_HEADER = "✨ <b><u>Hᴇʟᴘ Gᴜɪᴅᴇ Mᴇɴᴜ</u></b>\n\n💡 <b>Nᴏᴛᴇ: <i>Cʟɪᴄᴋ ᴏɴ ᴀɴʏ CMD ᴛᴏ sᴇᴇ ᴅᴇᴛᴀɪʟs.</i></b>"

    # async def stats(client, message):
    BOT_STATS = """<b>╭ ⌬ <u>𝘽𝙊𝙏 𝙎𝙏𝘼𝙏𝙎</u></b>
<b>┊</b>
<b>┊</b> 🕒 <b>𝐔𝐩𝐭𝐢𝐦𝐞:</b> {bot_uptime}
<b>┊</b>
<b>┊</b> 📊 <b><u>𝐑𝐀𝐌 𝐔𝐒𝐀𝐆𝐄</u></b>
<b>┊</b> {ram_bar} {ram}%
<b>┊</b> <b>𝐔𝐬𝐞𝐝:</b> {ram_u} | <b>𝐅𝐫𝐞𝐞:</b> {ram_f} | <b>𝐓𝐨𝐭𝐚𝐥:</b> {ram_t}
<b>┊</b>
<b>┊</b> 🔄 <b><u>𝐒𝐖𝐀𝐏 𝐌𝐄𝐌𝐎𝐑𝐘</u></b>
<b>┊</b> {swap_bar} {swap}%
<b>┊</b> <b>𝐔𝐬𝐞𝐝:</b> {swap_u} | <b>𝐅𝐫𝐞𝐞:</b> {swap_f} | <b>𝐓𝐨𝐭𝐚𝐥:</b> {swap_t}
<b>┊</b>
<b>┊</b> 💽 <b><u>𝐃𝐈𝐒𝐊 𝐒𝐓𝐀𝐓𝐒</u></b>
<b>┊</b> {disk_bar} {disk}%
<b>┊</b> <b>𝐑𝐞𝐚𝐝:</b> {disk_read} | <b>𝐖𝐫𝐢𝐭𝐞:</b> {disk_write}
<b>┊</b> <b>𝐔𝐬𝐞𝐝:</b> {disk_u} | <b>𝐅𝐫𝐞𝐞:</b> {disk_f} | <b>𝐓𝐨𝐭𝐚𝐥:</b> {disk_t}
<b>╰ ⚡𝗛𝗘𝗠𝗔𝗡𝗧𝗛⚡</b>
    """
    SYS_STATS = """<b>╭━━「 🖥 𝐒𝐘𝐒𝐓𝐄𝐌 𝐈𝐍𝐅𝐎 」</b>
<b>┃</b>
<b>┃</b> 🕒 <b>𝐎𝐒 𝐔𝐩𝐭𝐢𝐦𝐞:</b> {os_uptime}
<b>┃</b> 💿 <b>𝐎𝐒 𝐕𝐞𝐫𝐬𝐢𝐨𝐧:</b> {os_version}
<b>┃</b> 🏗 <b>𝐎𝐒 𝐀𝐫𝐜𝐡:</b> {os_arch}
<b>┃</b>
<b>┃</b> 🌐 <b><u>𝐍𝐄𝐓𝐖𝐎𝐑𝐊 𝐒𝐓𝐀𝐓𝐒</u></b>
<b>┃</b> 🔼 <b>𝐔𝐩:</b> {up_data} | 🔽 <b>𝐃𝐥:</b> {dl_data}
<b>┃</b> 📤 <b>𝐒𝐞𝐧𝐭:</b> {pkt_sent}ᴋ | 📥 <b>𝐑𝐞𝐜𝐯:</b> {pkt_recv}ᴋ
<b>┃</b> 📊 <b>𝐓𝐨𝐭𝐚𝐥 𝐈/𝐎:</b> {tl_data}
<b>┃</b>
<b>┃</b> 💻 <b><u>𝐂𝐏𝐔 𝐔𝐒𝐀𝐆𝐄</u></b>
<b>┃</b> {cpu_bar} {cpu}%
<b>┃</b> ⚡ <b>𝐅𝐫𝐞𝐪𝐮𝐞𝐧𝐜𝐲:</b> {cpu_freq}
<b>┃</b> 📈 <b>𝐀𝐯𝐠 𝐋𝐨𝐚𝐝:</b> {sys_load}
<b>┃</b> 🧠 <b>𝐂𝐨𝐫𝐞𝐬:</b> {p_core}𝐏 + {v_core}𝐕 | <b>𝐓𝐨𝐭𝐚𝐥:</b> {total_core}
<b>┃</b> 🛠 <b>𝐔𝐬𝐚𝐛𝐥𝐞:</b> {cpu_use} CPUs
<b>╰━━━━━━━━━━━━━━</b>
    """
    REPO_STATS = """📂 <b><u>Rᴇᴘᴏ Iɴғᴏ</u></b>
┠ <b>Lᴀsᴛ Uᴘᴅᴀᴛᴇ:</b> {last_commit}
┠ <b>Vᴇʀsɪᴏɴ:</b> {bot_version}
┠ <b>Lᴀᴛᴇsᴛ:</b> {lat_version}
┖ <b>CʜᴀɴɢᴇLᴏɢ:</b> {commit_details}

📝 <b>Rᴇᴍᴀʀᴋs:</b> <code>{remarks}</code>
    """
    BOT_LIMITS = """🚫 <b><u>Bᴏᴛ Lɪᴍɪᴛᴀᴛɪᴏɴs</u></b>
┠ <b>Dɪʀᴇᴄᴛ:</b> {DL} Gʙ
┠ <b>Tᴏʀʀᴇɴᴛ:</b> {TL} Gʙ
┠ <b>GDʀɪᴠᴇ:</b> {GL} Gʙ
┠ <b>YT-DLP:</b> {YL} Gʙ
┠ <b>Pʟᴀʏʟɪsᴛ:</b> {PL}
┠ <b>Mᴇɢᴀ:</b> {ML} Gʙ
┠ <b>Cʟᴏɴᴇ:</b> {CL} Gʙ
┖ <b>Lᴇᴇᴄʜ:</b> {LL} Gʙ

🔑 <b><u>Usᴇʀ Lɪᴍɪᴛs</u></b>
┠ <b>Tᴏᴋᴇɴ Vᴀʟɪᴅɪᴛʏ:</b> {TV}
┠ <b>Tɪᴍᴇ Gᴀᴘ:</b> {UTI}
┠ <b>Usᴇʀ Tᴀsᴋs:</b> {UT}
┖ <b>Bᴏᴛ Tᴀsᴋs:</b> {BT}
    """
    # ---------------------

    # async def restart(client, message): ---> __main__.py
    RESTARTING = "<i>Restarting...</i>"
    # ---------------------

    # async def restart_notification(): ---> __main__.py
    RESTART_SUCCESS = """⌬ <b><i>Restarted Successfully!</i></b>
┠ <b>Date:</b> {date}
┠ <b>Time:</b> {time}
┠ <b>TimeZone:</b> {timz}
┖ <b>Version:</b> {version}"""
    RESTARTED = """⌬ <b><i>Bot Restarted!</i></b>"""
    # ---------------------

    # async def ping(client, message): ---> __main__.py
    PING = "<i>Starting Ping..</i>"
    PING_VALUE = "<b>Pong</b>\n<code>{value} ms..</code>"
    # ---------------------

    # async def onDownloadStart(self): --> tasks_listener.py
    LINKS_START = """<b><i>Task Started</i></b>
┠ <b>Mode:</b> {Mode}
┖ <b>By:</b> {Tag}\n\n"""
    LINKS_SOURCE = """➲ <b>Source:</b>
┖ <b>Added On:</b> {On}
------------------------------------------
{Source}
------------------------------------------\n\n"""

    # async def __msg_to_reply(self): ---> pyrogramEngine.py
    PM_START = "➲ <b><u>Task Started :</u></b>\n┃\n┖ <b>Link:</b> <a href='{msg_link}'>Click Here</a>"
    L_LOG_START = "➲ <b><u>Leech Started :</u></b>\n┃\n┠ <b>User :</b> {mention} ( #ID{uid} )\n┖ <b>Source :</b> <a href='{msg_link}'>Click Here</a>"

    # async def onUploadComplete(): ---> tasks_listener.py
    NAME = "<b><i>{Name}</i></b>\n┃\n"
    SIZE = "┠ <b>𝐒𝐢𝐳𝐞: </b>{Size}\n"
    ELAPSE = "┠ <b>𝐄𝐥𝐚𝐩𝐬𝐞𝐝: </b>{Time}\n"
    MODE = "┠ <b>𝐌𝐨𝐝𝐞: </b>{Mode}\n"

    # ----- LEECH -------
    L_TOTAL_FILES = "┠ <b>𝐓𝐨𝐭𝐚𝐥 𝐅𝐢𝐥𝐞𝐬: </b>{Files}\n"
    L_CORRUPTED_FILES = "┠ <b>𝐂𝐨𝐫𝐫𝐮𝐩𝐭𝐞𝐝 𝐅𝐢𝐥𝐞𝐬: </b>{Corrupt}\n"
    L_CC = "┖ <b>𝐁𝐲: </b>{Tag}\n\n"
    PM_BOT_MSG = "➲ <b><i>File(s) have been Sent above</i></b>"
    L_BOT_MSG = "➲ <b><i>File(s) have been Sent to Bot PM (Private)</i></b>"
    L_LL_MSG = "➲ <b><i>File(s) have been Sent. Access via Links...</i></b>\n"

    # ----- MIRROR -------
    M_TYPE = "┠ <b>𝐓𝐲𝐩𝐞: </b>{Mimetype}\n"
    M_SUBFOLD = "┠ <b>𝐒𝐮𝐛𝐅𝐨𝐥𝐝𝐞𝐫𝐬: </b>{Folder}\n"
    TOTAL_FILES = "┠ <b>𝐅𝐢𝐥𝐞𝐬: </b>{Files}\n"
    RCPATH = "┠ <b>𝐏𝐚𝐭𝐡: </b><code>{RCpath}</code>\n"
    M_CC = "┖ <b>𝐁𝐲: </b>{Tag}\n\n"
    M_BOT_MSG = "➲ <b><i>Link(s) have been Sent to Bot PM (Private)</i></b>"
    # ----- BUTTONS -------
    CLOUD_LINK = "☁️ Cloud Link"
    SAVE_MSG = "📨 Save Message"
    RCLONE_LINK = "♻️ RClone Link"
    DDL_LINK = "📎 {Serv} Link"
    SOURCE_URL = "🔐 Source Link"
    INDEX_LINK_F = "🗂 Index Link"
    INDEX_LINK_D = "⚡ Index Link"
    VIEW_LINK = "🌐 View Link"
    CHECK_PM = "📥 View in Bot PM"
    CHECK_LL = "🖇 View in Links Log"
    MEDIAINFO_LINK = "📃 MediaInfo"
    SCREENSHOTS = "🖼 ScreenShots"
    # ---------------------

    # def get_readable_message(): ---> bot_utilis.py
    ####--------OVERALL MSG HEADER----------
    STATUS_NAME = "<b><i>{Name}</i></b>"

    #####---------PROGRESSIVE STATUS-------
    BAR = "\n<b>╭ Progress:</b> {Bar} » {Pct}%"
    PROCESSED = "\n<b>┊ Processed:</b> 📦 {Processed}"
    TOTAL_SIZE = "\n<b>┊ Total:</b> 📁 {Total}"
    STATUS = '\n<b>┊ Status:</b> {Status_Icon} <a href="{Url}">{Status}...</a>'
    ETA = "\n<b>┊ ETA:</b> ⏳ {Eta}"
    SPEED = "\n<b>┊ Speed:</b> ⚡ {Speed}"
    ELAPSED = " | <b>Elapsed:</b> ⏱️ {Elapsed}"
    ENGINE = "\n<b>┊ Engine:</b> 🔧 {Engine}"
    UPLOAD = "\n<b>┊ Upload:</b> 📤 {Upload}"
    STA_MODE = "\n<b>┊ Mode:</b> 🔄 {Mode}"
    SEEDERS = "\n<b>Seeders:</b> {Seeders} | "
    LEECHERS = "<b>Leechers:</b> {Leechers}"

    ####--------SEEDING----------
    SEED_SIZE = "\n<b>Size: </b>{Size}"
    SEED_SPEED = "\n<b>Speed: </b> {Speed} | "
    UPLOADED = "<b>Uploaded: </b> {Upload}"
    RATIO = "\n<b>Ratio: </b> {Ratio} | "
    TIME = "<b>Time: </b> {Time}"
    SEED_ENGINE = "\n<b>Engine:</b> {Engine}"

    ####--------NON-PROGRESSIVE + NON SEEDING----------
    STATUS_SIZE = "\n<b>Size: </b>{Size}"
    NON_ENGINE = "\n<b>Engine:</b> {Engine}"

    ####--------OVERALL MSG FOOTER----------
    USER = "\n<b>┊ User:</b> 👤 {User}"
    BTSEL = "\n<b>┊ Select:</b> {Btsel}"
    CANCEL = "\n<b>╰</b> {Cancel}\n\n"

    ####------FOOTER--------
    FOOTER = "<b>「 🌟 BOT STATS 」</b>\n"
    TASKS = "📥 <b>Tasks:</b> {Tasks}\n"
    BOT_TASKS = "📤 <b>Tasks:</b> {Tasks}/{Ttask} | <b>AVL:</b> {Free}\n"
    Cpu = "💻 <b>CPU:</b> {cpu}% | "
    FREE = "<b>Free:</b> {free} [{free_p}%]"
    Ram = "\n📊 <b>RAM:</b> {ram}% | "
    uptime = "<b>UP:</b> {uptime}"
    DL = "\n🔽 <b>DL:</b> {DL}/s | "
    UL = "🔼 <b>UL:</b> {UL}/s"

    ###--------BUTTONS-------
    PREVIOUS = "⫷"
    REFRESH = "ᴘᴀɢᴇs\n{Page}"
    NEXT = "⫸"
    # ---------------------

    # STOP_DUPLICATE_MSG: ---> clone.py, aria2_listener.py, task_manager.py
    STOP_DUPLICATE = (
        "File/Folder is already available in Drive.\nHere are {content} list results:"
    )
    # ---------------------

    # async def countNode(_, message): ----> gd_count.py
    COUNT_MSG = "<b>Counting:</b> <code>{LINK}</code>"
    COUNT_NAME = "<b><i>{COUNT_NAME}</i></b>\n┃\n"
    COUNT_SIZE = "┠ <b>Size: </b>{COUNT_SIZE}\n"
    COUNT_TYPE = "┠ <b>Type: </b>{COUNT_TYPE}\n"
    COUNT_SUB = "┠ <b>SubFolders: </b>{COUNT_SUB}\n"
    COUNT_FILE = "┠ <b>Files: </b>{COUNT_FILE}\n"
    COUNT_CC = "┖ <b>By: </b>{COUNT_CC}\n"
    # ---------------------

    # LIST ---> gd_list.py
    LIST_SEARCHING = "<b>Searching for <i>{NAME}</i></b>"
    LIST_FOUND = "<b>Found {NO} result for <i>{NAME}</i></b>"
    LIST_NOT_FOUND = "No result found for <i>{NAME}</i>"
    # ---------------------

    # async def mirror_status(_, message): ----> status.py
    NO_ACTIVE_DL = """<i>No Active Downloads!</i>
    
⌬ <b><i>Bot Stats</i></b>
┠ <b>CPU:</b> {cpu}% | <b>F:</b> {free} [{free_p}%]
┖ <b>RAM:</b> {ram} | <b>UPTIME:</b> {uptime}
    """
    # ---------------------

    # USER Setting --> user_setting.py
    USER_SETTING = """🌈 <b><u>𝐏𝐫𝐞𝐦𝐢𝐮𝐦 𝐔𝐬𝐞𝐫 𝐒𝐞𝐭𝐭𝐢𝐧𝐠𝐬</u></b>
        
👤<b> 𝐍𝐚𝐦𝐞 :</b> {NAME} ( <code>{ID}</code> )
🆔<b> 𝐔𝐬𝐞𝐫𝐧𝐚𝐦𝐞 :</b> {USERNAME}
🌐<b> 𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐦 DC :</b> {DC}
🌍<b> 𝐋𝐚𝐧𝐠𝐮𝐚𝐠𝐞 :</b> {LANG}

🛠 <u><b>𝐀𝐯𝐚𝐢𝐥𝐚𝐛𝐥𝐞 𝐀𝐫𝐠𝐬:</b></u>
• <b>-s</b> or <b>-set</b>: 𝐒𝐞𝐭 𝐃𝐢𝐫𝐞𝐜𝐭𝐥𝐲 𝐯𝐢𝐚 𝐀𝐫𝐠"""

    UNIVERSAL = """🎨 <b><u>𝐔𝐧𝐢𝐯𝐞𝐫𝐬𝐚𝐥 𝐒𝐞𝐭𝐭𝐢𝐧𝐠𝐬 : {NAME}</u></b>

⚙️<b> YT-DLP 𝐎𝐩𝐭𝐢𝐨𝐧𝐬 :</b> <b><code>{YT}</code></b>
📅<b> 𝐃𝐚𝐢𝐥𝐲 𝐓𝐚𝐬𝐤𝐬 :</b> <code>{DT}</code> ᴘᴇʀ ᴅ𝐚ʏ
🕒<b> 𝐋𝐚𝐬𝐭 𝐁𝐨𝐭 𝐔𝐬𝐞𝐝 :</b> <code>{LAST_USED}</code>
🔐<b> 𝐔𝐬𝐞𝐫 𝐒𝐞𝐬𝐬𝐢𝐨𝐧 :</b> <code>{USESS}</code>
📊<b> 𝐌𝐞𝐝𝐢𝐚𝐈𝐧𝐟𝐨 𝐌𝐨𝐝𝐞 :</b> <code>{MEDIAINFO}</code>
💾<b> 𝐒𝐚𝐯𝐞 𝐌𝐨𝐝𝐞 :</b> <code>{SAVE_MODE}</code>
📥<b> 𝐔𝐬𝐞𝐫 𝐁𝐨𝐭 PM :</b> <code>{BOT_PM}</code>"""

    MIRROR = """💎 <b><u>𝐌𝐢𝐫𝐫𝐨𝐫/𝐂𝐥𝐨𝐧𝐞 𝐒𝐞𝐭𝐭𝐢𝐧𝐠𝐬 : {NAME}</u></b>

📂<b> RClᴏɴᴇ 𝐂𝐨𝐧𝐟𝐢𝐠 :</b> <i>{RCLONE}</i>
🔼<b> 𝐌𝐢𝐫𝐫𝐨𝐫 𝐏𝐫𝐞𝐟𝐢𝐱 :</b> <code>{MPREFIX}</code>
🔽<b> 𝐌𝐢𝐫𝐫𝐨𝐫 𝐒𝐮𝐟𝐟𝐢𝐱 :</b> <code>{MSUFFIX}</code>
✂️<b> 𝐌𝐢𝐫𝐫𝐨𝐫 𝐑𝐞𝐦𝐧𝐚𝐦𝐞 :</b> <code>{MREMNAME}</code>
🔌<b> DDL 𝐒𝐞𝐫𝐯𝐞𝐫(𝐬) :</b> <i>{DDL_SERVER}</i>
⚡<b> 𝐔𝐬𝐞𝐫 TD 𝐌𝐨𝐝𝐞 :</b> <i>{TMODE}</i>
📑<b> 𝐓𝐨𝐭𝐚𝐥 𝐔𝐬𝐞𝐫 TD(𝐬) :</b> <i>{USERTD}</i>
🔑<b> 𝐃𝐫𝐢𝐯𝐞 𝐓𝐨𝐤𝐞𝐧 :</b> <i>{TOKEN}</i>
☁️<b> 𝐌𝐄𝐆𝐀 𝐂𝐫𝐞𝐝𝐬 :</b> <i>{MEGA}</i>
🌐<b> 𝐃𝐫𝐢𝐯𝐞 𝐋𝐢𝐧𝐤 :</b> <i>{DRIVE_LINK}</i>
📉<b> 𝐃𝐚𝐢𝐥𝐲 𝐌𝐢𝐫𝐫𝐨𝐫 :</b> <code>{DM}</code> ᴘᴇʀ ᴅ𝐚ʏ"""

    LEECH = """🔥 <b><u>𝐋𝐞𝐞𝐜𝐡 𝐒𝐞𝐭𝐭𝐢𝐧𝐠𝐬 𝐟𝐨𝐫 {NAME}</u></b>

📈<b> 𝐃𝐚𝐢𝐥𝐲 𝐋𝐞𝐞𝐜𝐡 : </b><code>{DL}</code> ᴘᴇʀ ᴅ𝐚ʏ
🏷<b> 𝐋𝐞𝐞𝐜𝐡 𝐓𝐲𝐩𝐞 :</b> <i>{LTYPE}</i>
🖼<b> 𝐂𝐮𝐬𝐭𝐨𝐦 𝐓𝐡𝐮𝐦𝐛𝐧𝐚𝐢𝐥 :</b> <i>{THUMB}</i>
📏<b> 𝐋𝐞𝐞𝐜𝐡 𝐒𝐩𝐥𝐢𝐭 𝐒𝐢𝐳𝐞 :</b> <code>{SPLIT_SIZE}</code>
🔀<b> 𝐄𝐪𝐮𝐚𝐥 𝐒𝐩𝐥𝐢𝐭𝐬 :</b> <i>{EQUAL_SPLIT}</i>
📦<b> 𝐌𝐞𝐝𝐢𝐚 𝐆𝐫𝐨𝐮𝐩 :</b> <i>{MEDIA_GROUP}</i>
📝<b> 𝐋𝐞𝐞𝐜𝐡 𝐂𝐚𝐩𝐭𝐢𝐨𝐧 :</b> <code>{LCAPTION}</code>
➕<b> 𝐋𝐞𝐞𝐜𝐡 𝐏𝐫𝐞𝐟𝐢𝐱 :</b> <code>{LPREFIX}</code>
➖<b> 𝐋𝐞𝐞𝐜𝐡 𝐒𝐮𝐟𝐟𝐢𝐱 :</b> <code>{LSUFFIX}</code>
📂<b> 𝐋𝐞𝐞𝐜𝐡 𝐃𝐮𝐦𝐩𝐬 :</b> <code>{LDUMP}</code>
🧪<b> 𝐋𝐞𝐞𝐜𝐡 𝐑𝐞𝐦𝐧𝐚𝐦𝐞 :</b> <code>{LREMNAME}</code>
✍️<b> 𝐀𝐮𝐭𝐨 𝐑𝐞𝐧𝐚𝐦𝐞 :</b> <code>{LAUTORENAME}</code>
🆔<b> 𝐋𝐞𝐞𝐜𝐡 𝐌𝐞𝐭𝐚𝐝𝐚𝐭𝐚 :</b> <code>{LMETA}</code>
🔗<b> 𝐋𝐞𝐞𝐜𝐡 𝐌𝐞𝐫𝐠𝐞 :</b> <i>{LMERGE}</i>
⌨️<b> FFmpeg CMDS :</b> <i>Available</i>"""

    AUDIO_SETTING = """🎬 <b><u>Media Tools Settings:</u></b>

┌<b>Audio Change:</b> <code>{AUDIO_CHANGE}</code>
├<b>Default Audio:</b> <code>{DEFAULT_AUDIO}</code>
├<b>Video Bitrate:</b> <code>{BITRATE}</code>
├<b>Video Watermark:</b> <code>{WATERMARK}</code>
├<b>Subtitle Sync:</b> <code>{SUBSYNC}</code>
├<b>Auto Merge ZIP:</b> <code>{AMERGE}</code>
├<b>Intro Video:</b> <code>{INTRO}</code>
└<b>MKV Attachments:</b> <code>{ATTACH}</code>"""
