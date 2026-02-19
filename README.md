<p align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&pause=1000&color=F70000&center=true&vCenter=true&width=435&lines=⚡+𝗛𝗘𝗠𝗔𝗡𝗧𝗛+⚡+-+𝗫;𝗠𝗜𝗥𝗥𝗢𝗥+-+𝗟𝗘𝗘𝗖𝗛+𝗕𝗢𝗧;𝗨𝗟𝗧𝗥𝗔+𝗙𝗔𝗦𝗧+𝗗𝗘𝗣𝗟𝗢𝗬𝗠𝗘𝗡𝗧" alt="Typing SVG" />
</p>

<p align="center">
  <img src="https://raw.githubusercontent.com/arjunrajrock7-creator/LEECHPRO7/master/Images/leechpro_banner.png" alt="LEECHPRO7 Banner" width="800">
</p>

<div align="center">

  [![Telegram Group](https://img.shields.io/badge/Telegram-Group-blue.svg?logo=telegram)](https://t.me/ALONEKINGSTAR77)
  [![GitHub Repo](https://img.shields.io/badge/GitHub-Repo-black.svg?logo=github)](https://github.com/arjunrajrock7-creator/LEECHPRO7)
  [![License](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

</div>

---

# 🚀 Welcome to ⚡𝗛𝗘𝗠𝗔𝗡𝗧𝗛⚡

The most powerful and feature-rich Telegram Mirror-Leech bot, optimized for ultra-high speed and 100% deployment success rate on **Heroku**, **Koyeb**, **VPS**, and **Render**.

### 🌟 Key Features
- ⚡ **Ultra Speed Boost**: Optimized multi-threaded Aria2 and qBittorrent configurations.
- 📁 **Cloud Support**: Seamlessly Mirror/Leech to Google Drive and other cloud storages.
- 🛠️ **Metadata Editor**: Custom General, Video, Audio, and Subtitle tags.
- 🔄 **Auto Rename**: Smart renaming with placeholders like `{season}`, `{episode}`, `{quality}`.
- 🎞️ **Media Tools**: Intro injection, watermark support, and MKV attachment management.
- 📱 **Mobile Optimized**: One-click deployment for DaRemote and Termius users.
- 🔗 **Advanced Merging**: Use `/merge2` with `-i` and `-n` flags for precise file combining.
- 🔊 **Audio Selector**: Interactive `/audio` tool to manage and remove unwanted audio tracks.

---

## 🛠️ Environment Variables Setup

| Variable | Description |
|----------|-------------|
| `BOT_TOKEN` | Your Telegram Bot Token from @BotFather |
| `OWNER_ID` | Your Telegram User ID |
| `TELEGRAM_API` | Your App ID from my.telegram.org |
| `TELEGRAM_HASH` | Your App Hash from my.telegram.org |
| `DATABASE_URL` | Your MongoDB connection string |
| `LEECH_DEST` | Default Leech destination (True for DM, False for Group) |
| `FFMPEG_CMDS` | Dictionary of preset FFmpeg commands |

---

## 📦 Deployment Guides

### 🐧 VPS Deployment (Recommended)
1. `sudo apt update && sudo apt upgrade -y`
2. `sudo apt install docker.io docker-compose -y`
3. `git clone https://github.com/arjunrajrock7-creator/LEECHPRO7 && cd LEECHPRO7`
4. `cp config_sample.env config.env` (Update your variables)
5. `docker-compose up -d --build`

### 📱 Termux Deployment
1. `pkg update && pkg upgrade -y`
2. `pkg install python ffmpeg aria2 git -y`
3. `git clone https://github.com/arjunrajrock7-creator/LEECHPRO7 && cd LEECHPRO7`
4. `pip install -r requirements.txt`
5. `python3 -m bot`

---

## 🎮 Commands List

- `/mirror2`: Mirror link/file to GDrive.
- `/leech2`: Leech link/file to Telegram.
- `/audio2`: Analyze and manage audio tracks (Reply to file).
- `/merge2`: Merge multiple files.
- `/usetting2`: User settings menu.
- `/bsetting2`: Bot settings (Sudo only).

### ☁️ Heroku Deployment (Recommended)
1. **Container Registry Method**:
   ```bash
   heroku container:login
   heroku create your-app-name
   heroku container:push web -a your-app-name
   heroku container:release web -a your-app-name
   ```
2. **Config Vars**: Add all mandatory variables in Heroku Dashboard.

### ☁️ Koyeb Deployment
- Connect your GitHub and select the `LEECHPRO7` repository.
- Select **Docker** as the builder.
- Add your variables and set port to `8000`.

### 🖥️ VPS & Mobile Deployment (DaRemote/Termius)
- Create a `config.env` file in your root directory.
- Run this command in your terminal:
  ```bash
  wget https://raw.githubusercontent.com/arjunrajrock7-creator/LEECHPRO7/master/deploy_vps.vs && bash deploy_vps.vs
  ```
- **DaRemote Instructions**:
  1. Open DaRemote and connect to your VPS.
  2. Navigate to "Commands" and paste the deploy script.
  3. Ensure 100% success rate by using a clean Ubuntu/Debian environment.

---

## ⌨️ Custom FFmpeg Commands (`FFMPEG_CMDS`)

You can set multiple FFmpeg command sets in your user settings.
- **Format:** `{"key": ["cmd1", "cmd2"]}`
- **Usage:** `/cmd -ff key`

### 💡 Placeholders:
- `mltb.mkv`: Matches only `.mkv` files.
- `mltb.video`: Matches all video formats.
- `mltb.audio`: Matches all audio formats.
- `mltb`: Reference to the original file (matches all).
- `-del`: Add to a command to delete the source file after successful processing.

**Example:**
`{"subtitle": ["-i mltb.mkv -c copy -c:s srt mltb.mkv", "-i mltb.video -c copy -c:s srt mltb"]}`

---

## ⌬ Video Tool Usage Guide

To access the Video Tool menu, use the `-vt` argument in your command.

**Options included:**
✔ Encode, Watermark, Merge V+A, Merge V+S, Hardsub, Extract, Swap Audio, Convert, Filters, Intro.

**Examples:**
- `/cmd -vt`
- External Merge: `/cmd -i 10 -m "Your File Name" -vt`
- Apply FFmpeg key: `/cmd -vt -ff metadata`

---

## 📤 Upload Mode (DM vs Group)

Configure this in `/usetting2`.
- **Bot DM**: Files sent directly to your private chat.
- **Group**: Files sent to the authorized group ID.

---

## 🛠 Advanced Troubleshooting

- **NoneType Errors**: Fixed by fallback to `sender_chat`.
- **Stuck Tasks**: Use `/cancel2` and check logs.
- **FFmpeg Fails**: Check if command syntax is correct in `FFMPEG_CMDS`.

---

<p align="center">
  <img src="https://img.shields.io/badge/Developed%20with%20❤️%20by-⚡𝗛𝗘𝗠𝗔𝗡𝗧𝗛⚡-red" alt="Developer Info">
</p>

<p align="center">
  <b>Support Channel:</b> <a href="https://t.me/ALONEKINGSTAR77">@ALONEKINGSTAR77</a>
</p>
