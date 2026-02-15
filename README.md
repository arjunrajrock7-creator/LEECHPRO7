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

### ☁️ Heroku Deployment (Dockerfile Method)
1. **Install Heroku CLI**: Make sure you have the Heroku CLI installed on your machine.
2. **Login to Heroku**:
   ```bash
   heroku login
   heroku container:login
   ```
3. **Create a New App**:
   ```bash
   heroku create your-app-name
   ```
4. **Setup Config Vars**:
   - Go to Heroku Dashboard -> Settings -> Reveal Config Vars.
   - Add all mandatory variables from `config.env`.
5. **Push and Release Container**:
   ```bash
   heroku container:push web -a your-app-name
   heroku container:release web -a your-app-name
   ```
6. **Alternative (Buildpacks)**: If you prefer not using Docker, add `heroku/python` and `https://github.com/jonathanong/heroku-buildpack-ffmpeg-latest.git` buildpacks.

### 📱 Mobile SSH Deployment (DaRemote/Termius)
1. **Prepare your VPS**: Ensure you have a Linux VPS (Ubuntu/Debian recommended).
2. **One-Click Deployment**: Run the following command in your mobile SSH client:
   ```bash
   wget https://raw.githubusercontent.com/ALONEKINGSTAR77/WZML-X/master/deploy_vps.sh && bash deploy_vps.sh
   ```
3. **What it does**: This script automates everything:
   - Updates your system.
   - Installs Docker and Docker-Compose.
   - Clones the repository.
   - Sets up a sample `config.env`.
   - Starts the bot in the background using Docker.
4. **Final Step**: After running the script, edit your `config.env` using `nano config.env`, add your credentials, and restart with `docker-compose restart`.

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
