# ⚡𝗛𝗘𝗠𝗔𝗡𝗧𝗛⚡ Mirror-Leech Bot

A powerful, high-performance Telegram bot to mirror, leech, and process media files with FFmpeg. Optimized for speed and reliability.

## 🚀 Key Features
- **Mirror & Leech**: Support for GDrive, RClone, and direct Telegram uploads.
- **🔀 Video Merging**: Automatically merge multiple videos into a single high-quality MKV.
- **🗜️ Advanced Compression**: Aggressive yet high-quality video compression tools.
- **⌨️ Custom FFmpeg Commands**: Set your own FFmpeg parameters directly from the bot settings.
- **⚡ Performance Boosted**: Async architecture, multi-threading, and hardware acceleration enabled.
- **📱 Multi-Platform Deployment**: Support for VPS, Heroku, Docker, and Termux.

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

### 🖥️ VPS Deployment (Ubuntu/Debian)
1. **Update and Install Dependencies**:
   ```bash
   sudo apt update && sudo apt upgrade -y
   sudo apt install git python3 python3-pip ffmpeg -y
   ```
2. **Clone the Repository**:
   ```bash
   git clone https://github.com/ALONEKINGSTAR77/WZML-X.git && cd WZML-X
   ```
3. **Install Requirements**:
   ```bash
   pip3 install -r requirements.txt
   ```
4. **Setup config.env**:
   - Create a `config.env` file and fill in your variables.
5. **Start the Bot**:
   ```bash
   python3 -m bot
   ```

### 🐳 Docker Deployment (Recommended)
1. **Build & Run**:
   ```bash
   docker build -t hemanth-bot .
   docker run -p 8000:8000 hemanth-bot
   ```
   *Note: Ensure your `config.env` is present in the root directory.*

### ☁️ Heroku Deployment
1. **Create a New App**: Go to the Heroku Dashboard and create a new application.
2. **Add Buildpacks**: In the "Settings" tab, add the following buildpacks:
   - `heroku/python`
   - `https://github.com/jonathanong/heroku-buildpack-ffmpeg-latest.git`
3. **Configure Environment Variables**: In the "Settings" tab, click "Reveal Config Vars" and add:
   - `BOT_TOKEN`: Your Telegram Bot Token.
   - `OWNER_ID`: Your Telegram User ID.
   - `TELEGRAM_API`: Your App ID from my.telegram.org.
   - `TELEGRAM_HASH`: Your App Hash from my.telegram.org.
   - `DATABASE_URL`: Your MongoDB connection string.
   - `UPSTREAM_REPO`: (Optional) Your GitHub fork URL.
   - `PORT`: 8000 (Heroku will automatically assign a port, but the bot defaults to 8000 if not specified).
4. **Deploy Code**:
   - Connect your GitHub repository in the "Deploy" tab.
   - Select the branch and click "Deploy Branch".
5. **Enable Dynos**: In the "Resources" tab, ensure the `web` or `worker` dyno is switched ON.

### 📱 Termux (Android Mobile)
1. **Install Packages**:
   ```bash
   pkg update && pkg upgrade
   pkg install git python ffmpeg
   ```
2. **Follow VPS steps** (2 to 5).

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
**Powered by ⚡𝗛𝗘𝗠𝗔𝗡𝗧𝗛⚡**
