# 🎼 New ⚡𝗛𝗘𝗠𝗔𝗡𝗧𝗛⚡-X 🚀

📚 Library : Pyrofork
🌎 Language : Python 3
🛡 Database : MongoDB
🛠 Version : 2.0

🥶 Feature : M/L All Your Links | Files | Torrents to Aria2, qBit, Google Drive Support ⚡️

💎 User Settings ⚙️ :

┌ Thumbnail
├ Prefix
├ Suffix
├ Remname
├ Caption
├ Auto Rename
├ File Type -> Document or Media
└ Metadata Editor

🚀 Metadata Edit All Upload ‼️

┌ Remove Exists Metadata
├ General Metadata Tag
├ Video Metadata Tag
├ Audio Metadata Tag
└ Subtitle Video Tag

🚀 Attachment Upload ‼️

┌ Name
└ Url

🚀 Merge Video Update ‼️

┌ Merge : Enabled / Disabled
└ Merge + Original Files : Enabled / Disabled

- Merge video from GD/Torrent/Magnet 🪩
- Merge from zip with unzip cmd 🤡

🚀 File Merge Format ‼️

/l -i <count> -m <filename> -n

⁍ Rename file : -n
⁍ Zip files or Links : -z
⁍ Download bulk links : -b
⁍ Download multi links : -i
⁍ Join Multiple Files : -j
⁍ Extract/Unzip files from Archive : -e
⁍ Download multi links within same upload directory : -m

🕯 Note : QB commands only for torrents !

❤️‍🔥 Auto Rename Feature Update Successfully! 😇

✍️ Description : File Autorename is the Custom rename on the Files Uploaded by the bot.

➡️ Example Auto Rename:
{season} - Season Number
{episode} - Episode Number
{size} - File Size
{quality} - Quality

💎 Simple Auto Rename :
Stranger Things (2025) {season} {episode} - {quality} - NF WEB-DL - AVC - [Tamil +Telugu +Hindi + Eng] - H.264 (DDP5.1 - 192Kbps) - {size} - ESub

---

## ⚡ Ultra Speed Boost Features

- **Parallel Processing**: Optimized Gunicorn with multiple workers and threads for high concurrency.
- **CPU Optimization**: Automatic FFmpeg thread detection using all available CPU cores.
- **High-Speed Networking**: TCP optimization and BBR congestion control enabled in VPS deployment.
- **Multi-Threaded 7z**: Maximum compression and extraction speed using all CPU cores.
- **Aria2 & qBit Tweaks**: Pre-configured for ultra-high-speed downloads with optimized buffers and connection limits.
- **Fast Merging**: Instant MKV merging using stream copy (`-c copy`) whenever possible.

---

## 🛠️ Environment Variables Setup

Before deployment, ensure you have the following variables ready:

| Variable | Description |
|----------|-------------|
| `BOT_TOKEN` | Your Telegram Bot Token from @BotFather |
| `OWNER_ID` | Your Telegram User ID |
| `TELEGRAM_API` | Your App ID from my.telegram.org |
| `TELEGRAM_HASH` | Your App Hash from my.telegram.org |
| `DATABASE_URL` | Your MongoDB connection string |
| `UPSTREAM_REPO` | (Optional) Your GitHub fork URL for auto-updates |

---

## 📦 Deployment Guides

### ☁️ Koyeb Deployment (100% Success)
1. **Login to Koyeb**: Go to [Koyeb](https://app.koyeb.com/).
2. **Create a New Service**: Select 'GitHub' or 'Docker'.
3. **GitHub Method**:
   - Connect your GitHub and select the `LEECHPRO7` repository.
   - Select **Docker** as the builder.
   - In **Environment Variables**, add all mandatory keys from `config.env`.
   - **Crucial**: Set the **Port** to `8000`.
   - **Instance Type**: 'Nano' is enough for basic usage, but 'Small' is recommended for high-speed FFmpeg tasks.
   - Deploy.
4. **Docker Method**:
   - Use the image: `mysterysd/wzmlx:latest` or build your own.
   - Set the **Command** to `bash start.vs`.
   - Configure variables and port `8000`.

### ☁️ Heroku Deployment (High Performance)
1. **Install Heroku CLI**: Install it on your system.
2. **Login and Setup**:
   ```bash
   heroku login
   heroku container:login
   ```
3. **Create and Deploy**:
   ```bash
   heroku create your-app-name
   heroku container:push web -a your-app-name
   heroku container:release web -a your-app-name
   ```
4. **Config Vars**: Add all variables in Settings -> Reveal Config Vars.

### 🖥️ VPS Deployment (Manual)
1. **Dependencies**:
   ```bash
   sudo apt update && sudo apt install git python3 python3-pip ffmpeg -y
   ```
2. **Clone & Setup**:
   ```bash
   git clone https://github.com/arjunrajrock7-creator/LEECHPRO7.git && cd LEECHPRO7
   pip3 install -r requirements.txt
   ```
3. **Configure**: Create `config.env` with your details.
4. **Start**: `python3 -m bot` or use `pm2` / `screen`.

### 📱 Mobile & DaRemote Deployment (Auto)
1. **One-Click Command**: Run this in DaRemote or any SSH client:
   ```bash
   wget https://raw.githubusercontent.com/arjunrajrock7-creator/LEECHPRO7/master/deploy_vps.vs && bash deploy_vps.vs
   ```
2. **Setup**: This script installs Docker, clones the repo, and sets up high-speed optimizations.
3. **Finalize**: Edit `config.env` and run `docker-compose restart`.

### 🐳 Docker Deployment (Universal)
```bash
docker build -t leechpro7 .
docker run -p 8000:8000 --env-file config.env leechpro7
```

---

## ⚙️ FFmpeg Command Usage
You can set manual commands in `/usersettings` -> **Leech** -> **FFmpeg CMDS**.
- **Example**: `-c:v libx265 -crf 25 -preset fast`
- These commands will be applied to all video files processed by the bot.

## ❓ Troubleshooting
- **Freezing/Infinite Loading**: Ensure your VPS has enough RAM and CPU for FFmpeg tasks.
- **Database Errors**: Check if your MongoDB IP whitelist allows access from your bot's IP.
- **Merge Failures**: Ensure all video files are valid and not corrupted.

## 🤝 Support
Join our community for updates and support: [@ALONEKINGSTAR77](https://t.me/ALONEKINGSTAR77)

---
---
**Note:** This repository is pre-configured with a `config.env` file for a 100% success rate deployment on Heroku using the Dockerfile.

**Powered by ⚡𝗛𝗘𝗠𝗔𝗡𝗧𝗛⚡**
