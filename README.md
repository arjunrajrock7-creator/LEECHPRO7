# ⚡𝗛𝗘𝗠𝗔𝗡𝗧𝗛⚡ Mirror-Leech Bot

This is a powerful, high-performance Mirror-Leech bot designed to run on Heroku, Koyeb, VPS, and mobile platforms.

## 🚀 Deployment Guide

### ☁️ Deployment on Koyeb (Recommended)
1. **Create Account:** Sign up at [Koyeb](https://www.koyeb.com/).
2. **New Service:** Click "Create Service", select "GitHub".
3. **Repository:** Choose your forked repository.
4. **Environment Variables:**
   - Add `BOT_TOKEN`, `OWNER_ID`, `TELEGRAM_API`, `TELEGRAM_HASH`, `DATABASE_URL`.
   - The bot will automatically bind to the correct port.
5. **Deploy:** Click "Deploy".

### 💜 Deployment on Heroku
1. **Create App:** Go to Heroku Dashboard and create a new app.
2. **Buildpacks:**
   - `heroku/python`
   - `https://github.com/jonathanong/heroku-buildpack-ffmpeg-latest.git`
3. **Config Vars:** Fill in the variables from `config.env`.
4. **Deploy:** Use Heroku CLI or GitHub integration.

### 🖥️ Deployment on VPS (Ubuntu/Debian)
1. **Update System:**
   ```bash
   sudo apt update && sudo apt upgrade -y
   ```
2. **Install Docker:**
   ```bash
   curl -fsSL https://get.docker.com -o get-docker.sh
   sh get-docker.sh
   ```
3. **Clone Repo:**
   ```bash
   git clone https://github.com/ALONEKINGSTAR77/WZML-X.git
   cd WZML-X
   ```
4. **Configure:** Edit `config.env` with your values.
5. **Start:**
   ```bash
   docker-compose up --build -d
   ```

### 📱 Deployment on DaRemote (Mobile)
1. **Open DaRemote:** Add your VPS server.
2. **Terminal:** Follow the VPS steps above.
3. **One-Tap Setup:** Use the `deploy_vps.sh` script for even faster setup.
   ```bash
   bash deploy_vps.sh
   ```

## 🛠️ Video Tools usage
- Use `/usersettings` or `/uset` to access your personal settings.
- Navigate to **Audio Settings** or **Video Tools**.
- Configure Metadata, Merging, Bitrate, Watermark, and more.
- These settings will be applied automatically to all your tasks.

## ❓ Troubleshooting
- **Button Loading:** If buttons show a loading circle, ensure the bot is not under heavy flood wait. We have implemented an auto-answer fix.
- **Heroku Crash:** Check your `PORT` binding. The bot is optimized to use Heroku's dynamic port.
- **FFmpeg Errors:** Ensure `FFMPEG_THREADS` is set appropriately for your VPS (usually 2-4). On PaaS, leave it empty.

---
### 🛡️ Support & Community
- **Support Group**: [@ALONEKINGSTAR77](https://t.me/ALONEKINGSTAR77)
- **Updates**: [@ALONEKINGSTAR77](https://t.me/ALONEKINGSTAR77)
