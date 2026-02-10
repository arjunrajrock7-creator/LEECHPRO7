#!/usr/bin/env python3
class WZMLStyle:
    # ----------------------
    # async def start(client, message) ---> __main__.py
    ST_BN1_NAME = "Repo"
    ST_BN1_URL = "https://www.github.com/weebzone/WZML-X"
    ST_BN2_NAME = "Updates"
    ST_BN2_URL = "https://t.me/WZML_X"
    ST_MSG = """<i>This bot can mirror all your links|files|torrents to Google Drive or any rclone cloud or to telegram or to ddl servers.</i>
<b>Type {help_command} to get a list of available commands</b>"""
    ST_BOTPM = """<i>Now, This bot will send all your files and links here. Start Using ...</i>"""
    ST_UNAUTH = """<i>You Are not authorized user! Deploy your own WZML-X Mirror-Leech bot</i>"""
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
    BOT_STATS = """⚙️ <b><u>Bᴏᴛ Sᴛᴀᴛɪsᴛɪᴄs</u></b>
🕒 <b>Uᴘᴛɪᴍᴇ:</b> {bot_uptime}

📊 <b><u>Rᴀᴍ Usᴀɢᴇ</u></b>
{ram_bar} {ram}%
┖ <b>Usᴇᴅ:</b> {ram_u} | <b>Fʀᴇᴇ:</b> {ram_f} | <b>Tᴏᴛᴀʟ:</b> {ram_t}

🔄 <b><u>Sᴡᴀᴘ Mᴇᴍᴏʀʏ</u></b>
{swap_bar} {swap}%
┖ <b>Usᴇᴅ:</b> {swap_u} | <b>Fʀᴇᴇ:</b> {swap_f} | <b>Tᴏᴛᴀʟ:</b> {swap_t}

💽 <b><u>Dɪsᴋ Sᴛᴀᴛs</u></b>
{disk_bar} {disk}%
┠ <b>Rᴇᴀᴅ:</b> {disk_read} | <b>Wʀɪᴛᴇ:</b> {disk_write}
┖ <b>Usᴇᴅ:</b> {disk_u} | <b>Fʀᴇᴇ:</b> {disk_f} | <b>Tᴏᴛᴀʟ:</b> {disk_t}
    """
    SYS_STATS = """🖥 <b><u>Sʏsᴛᴇᴍ Iɴғᴏ</u></b>
┠ <b>OS Uᴘᴛɪᴍᴇ:</b> {os_uptime}
┠ <b>OS Vᴇʀsɪᴏɴ:</b> {os_version}
┖ <b>OS Aʀᴄʜ:</b> {os_arch}

🌐 <b><u>Nᴇᴛᴡᴏʀᴋ Sᴛᴀᴛs</u></b>
┠ <b>Uᴘʟᴏᴀᴅ:</b> {up_data} | <b>Dᴏᴡɴʟᴏᴀᴅ:</b> {dl_data}
┠ <b>Pᴋᴛs Sᴇɴᴛ:</b> {pkt_sent}ᴋ | <b>Rᴇᴄᴠ:</b> {pkt_recv}ᴋ
┖ <b>Tᴏᴛᴀʟ I/O:</b> {tl_data}

💻 <b><u>CPU Usᴀɢᴇ</u></b>
{cpu_bar} {cpu}%
┠ <b>Fʀᴇǫᴜᴇɴᴄʏ:</b> {cpu_freq}
┠ <b>Aᴠɢ Lᴏᴀᴅ:</b> {sys_load}
┠ <b>Cᴏʀᴇs:</b> {p_core}P + {v_core}V | <b>Tᴏᴛᴀʟ:</b> {total_core}
┖ <b>Usᴀʙʟᴇ:</b> {cpu_use} CPUs
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
    SIZE = "┠ <b>Size: </b>{Size}\n"
    ELAPSE = "┠ <b>Elapsed: </b>{Time}\n"
    MODE = "┠ <b>Mode: </b>{Mode}\n"

    # ----- LEECH -------
    L_TOTAL_FILES = "┠ <b>Total Files: </b>{Files}\n"
    L_CORRUPTED_FILES = "┠ <b>Corrupted Files: </b>{Corrupt}\n"
    L_CC = "┖ <b>By: </b>{Tag}\n\n"
    PM_BOT_MSG = "➲ <b><i>File(s) have been Sent above</i></b>"
    L_BOT_MSG = "➲ <b><i>File(s) have been Sent to Bot PM (Private)</i></b>"
    L_LL_MSG = "➲ <b><i>File(s) have been Sent. Access via Links...</i></b>\n"

    # ----- MIRROR -------
    M_TYPE = "┠ <b>Type: </b>{Mimetype}\n"
    M_SUBFOLD = "┠ <b>SubFolders: </b>{Folder}\n"
    TOTAL_FILES = "┠ <b>Files: </b>{Files}\n"
    RCPATH = "┠ <b>Path: </b><code>{RCpath}</code>\n"
    M_CC = "┖ <b>By: </b>{Tag}\n\n"
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
    BAR = "\n┃ {Bar}"
    PROCESSED = "\n┠ <b>Processed:</b> {Processed}"
    STATUS = '\n┠ <b>Status:</b> <a href="{Url}">{Status}</a>'
    ETA = " | <b>ETA:</b> {Eta}"
    SPEED = "\n┠ <b>Speed:</b> {Speed}"
    ELAPSED = " | <b>Elapsed:</b> {Elapsed}"
    ENGINE = "\n┠ <b>Engine:</b> {Engine}"
    STA_MODE = "\n┠ <b>Mode:</b> {Mode}"
    SEEDERS = "\n┠ <b>Seeders:</b> {Seeders} | "
    LEECHERS = "<b>Leechers:</b> {Leechers}"

    ####--------SEEDING----------
    SEED_SIZE = "\n┠ <b>Size: </b>{Size}"
    SEED_SPEED = "\n┠ <b>Speed: </b> {Speed} | "
    UPLOADED = "<b>Uploaded: </b> {Upload}"
    RATIO = "\n┠ <b>Ratio: </b> {Ratio} | "
    TIME = "<b>Time: </b> {Time}"
    SEED_ENGINE = "\n┠ <b>Engine:</b> {Engine}"

    ####--------NON-PROGRESSIVE + NON SEEDING----------
    STATUS_SIZE = "\n┠ <b>Size: </b>{Size}"
    NON_ENGINE = "\n┠ <b>Engine:</b> {Engine}"

    ####--------OVERALL MSG FOOTER----------
    USER = "\n┠ <b>User:</b> <code>{User}</code> | "
    ID = "<b>ID:</b> <code>{Id}</code>"
    BTSEL = "\n┠ <b>Select:</b> {Btsel}"
    CANCEL = "\n┖ {Cancel}\n\n"

    ####------FOOTER--------
    FOOTER = "🌟 <b><u>Bᴏᴛ Sᴛᴀᴛs</u></b>\n"
    TASKS = "┠ <b>Tᴀsᴋs:</b> {Tasks}\n"
    BOT_TASKS = "┠ <b>Tᴀsᴋs:</b> {Tasks}/{Ttask} | <b>AVL:</b> {Free}\n"
    Cpu = "┠ <b>CPU:</b> {cpu}% | "
    FREE = "<b>Fʀᴇᴇ:</b> {free} [{free_p}%]"
    Ram = "\n┠ <b>RAM:</b> {ram}% | "
    uptime = "<b>UP:</b> {uptime}"
    DL = "\n┖ <b>DL:</b> {DL}/s | "
    UL = "<b>UL:</b> {UL}/s"

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
    USER_SETTING = """✨ <b><u>Pʀᴇᴍɪᴜᴍ Usᴇʀ Sᴇᴛᴛɪɴɢs</u></b>
        
👤<b> Nᴀᴍᴇ :</b> {NAME} ( <code>{ID}</code> )
🆔<b> Usᴇʀɴᴀᴍᴇ :</b> {USERNAME}
🌐<b> Tᴇʟᴇɢʀᴀᴍ DC :</b> {DC}
🌍<b> Lᴀɴɢᴜᴀɢᴇ :</b> {LANG}

🛠 <u><b>Aᴠᴀɪʟᴀʙʟᴇ Aʀɢs:</b></u>
• <b>-s</b> or <b>-set</b>: Sᴇᴛ Dɪʀᴇᴄᴛʟʏ ᴠɪᴀ Aʀɢ"""

    UNIVERSAL = """🌟 <b><u>Uɴɪᴠᴇʀsᴀʟ Sᴇᴛᴛɪɴɢs : {NAME}</u></b>

⚙️<b> YT-DLP Oᴘᴛɪᴏɴs :</b> <b><code>{YT}</code></b>
📅<b> Dᴀɪʟʏ Tᴀsᴋs :</b> <code>{DT}</code> ᴘᴇʀ ᴅᴀʏ
🕒<b> Lᴀsᴛ Bᴏᴛ Usᴇᴅ :</b> <code>{LAST_USED}</code>
🔐<b> Usᴇʀ Sᴇssɪᴏɴ :</b> <code>{USESS}</code>
📊<b> MᴇᴅɪᴀIɴғᴏ Mᴏᴅᴇ :</b> <code>{MEDIAINFO}</code>
💾<b> Sᴀᴠᴇ Mᴏᴅᴇ :</b> <code>{SAVE_MODE}</code>
📥<b> Usᴇʀ Bᴏᴛ PM :</b> <code>{BOT_PM}</code>"""

    MIRROR = """🚀 <b><u>Mɪʀʀᴏʀ/Cʟᴏɴᴇ Sᴇᴛᴛɪɴɢs : {NAME}</u></b>

📂<b> RClᴏɴᴇ Cᴏɴғɪɢ :</b> <i>{RCLONE}</i>
🔼<b> Mɪʀʀᴏʀ Pʀᴇғɪx :</b> <code>{MPREFIX}</code>
🔽<b> Mɪʀʀᴏʀ Sᴜғғɪx :</b> <code>{MSUFFIX}</code>
✂️<b> Mɪʀʀᴏʀ Rᴇᴍɴᴀᴍᴇ :</b> <code>{MREMNAME}</code>
🔌<b> DDL Sᴇʀᴠᴇʀ(s) :</b> <i>{DDL_SERVER}</i>
⚡<b> Usᴇʀ TD Mᴏᴅᴇ :</b> <i>{TMODE}</i>
📑<b> Tᴏᴛᴀʟ Usᴇʀ TD(s) :</b> <i>{USERTD}</i>
📉<b> Dᴀɪʟʏ Mɪʀʀᴏʀ :</b> <code>{DM}</code> ᴘᴇʀ ᴅᴀʏ"""

    LEECH = """⚡ <b><u>Lᴇᴇᴄʜ Sᴇᴛᴛɪɴɢs ғᴏʀ {NAME}</u></b>

📈<b> Dᴀɪʟʏ Lᴇᴇᴄʜ : </b><code>{DL}</code> ᴘᴇʀ ᴅᴀʏ
🏷<b> Lᴇᴇᴄʜ Tʏᴘᴇ :</b> <i>{LTYPE}</i>
🖼<b> Cᴜsᴛᴏᴍ Tʜᴜᴍʙɴᴀɪʟ :</b> <i>{THUMB}</i>
📏<b> Lᴇᴇᴄʜ Sᴘʟɪᴛ Sɪᴢᴇ :</b> <code>{SPLIT_SIZE}</code>
🔀<b> Eǫᴜᴀʟ Sᴘʟɪᴛs :</b> <i>{EQUAL_SPLIT}</i>
📦<b> Mᴇᴅɪᴀ Gʀᴏᴜᴘ :</b> <i>{MEDIA_GROUP}</i>
📝<b> Lᴇᴇᴄʜ Cᴀᴘᴛɪᴏɴ :</b> <code>{LCAPTION}</code>
➕<b> Lᴇᴇᴄʜ Pʀᴇғɪx :</b> <code>{LPREFIX}</code>
➖<b> Lᴇᴇᴄʜ Sᴜғғɪx :</b> <code>{LSUFFIX}</code>
📂<b> Lᴇᴇᴄʜ Dᴜᴍᴘs :</b> <code>{LDUMP}</code>
🧪<b> Lᴇᴇᴄʜ Rᴇᴍɴᴀᴍᴇ :</b> <code>{LREMNAME}</code>
🆔<b> Lᴇᴇᴄʜ Mᴇᴛᴀᴅᴀᴛᴀ :</b> <code>{LMETA}</code>
🔗<b> Lᴇᴇᴄʜ Mᴇʀɢᴇ :</b> <i>{LMERGE}</i>"""
