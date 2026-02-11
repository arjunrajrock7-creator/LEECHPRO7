# ⚡𝗛𝗘𝗠𝗔𝗡𝗧𝗛⚡ Mirror-Leech Bot Deployment Guide

Welcome to the official deployment guide for the **⚡𝗛𝗘𝗠𝗔𝗡𝗧𝗛⚡ Mirror-Leech Bot**. Follow these steps carefully for a smooth, 100% success rate deployment.

---

## 🛠️ Prerequisites
Before starting, ensure you have:
- **Telegram API ID & Hash**: Get from [my.telegram.org](https://my.telegram.org).
- **Bot Token**: Get from [@BotFather](https://t.me/BotFather).
- **MongoDB Database URL**: Get a free cluster from [MongoDB Atlas](https://www.mongodb.com/cloud/atlas).
- **Owner ID**: Use [@userinfobot](https://t.me/userinfobot) to get your Telegram ID.

---

## 🚀 1. KOYEB DEPLOYMENT (Recommended)
Koyeb is highly recommended for its stability and ease of use.

### Step-by-Step:
1. **Fork this Repository**: Click the 'Fork' button at the top right of this page.
2. **Create a Koyeb Account**: Sign up at [koyeb.com](https://www.koyeb.com).
3. **Create a New Service**:
   - Click **'Create Service'**.
   - Select **'GitHub'** as the deployment method.
   - Choose your forked repository.
4. **Configure Service**:
   - **Service Type**: Web Service.
   - **Region**: Choose the closest to you.
   - **Plan**: Select a plan (Nano/Micro recommended).
5. **Environment Variables**:
   - Click **'Add Variable'** for each of these:
     - `BOT_TOKEN`: Your bot token.
     - `OWNER_ID`: Your Telegram ID.
     - `TELEGRAM_API`: Your API ID.
     - `TELEGRAM_HASH`: Your API Hash.
     - `DATABASE_URL`: Your MongoDB URL.
     - `PORT`: `8000` (Crucial for health checks).
     - `FFMPEG_THREADS`: `1` (Prevents freezing on small instances).
6. **Port Binding**:
   - Set Port to **8000**.
   - Health Check path to **/health**.
7. **Deploy**: Click **'Deploy'**. Once the status shows "Healthy", your bot is ready!

---

## 💜 2. HEROKU DEPLOYMENT
Heroku requires buildpacks to handle media processing.

### Step-by-Step:
1. **Fork this Repository**: Just like the Koyeb method.
2. **Create a Heroku App**:
   - Login to Heroku.
   - Click **'New'** -> **'Create new app'**.
3. **Add Buildpacks**:
   - Go to **'Settings'** -> **'Buildpacks'**.
   - Add `heroku/python`.
   - Add `https://github.com/jonathanong/heroku-buildpack-ffmpeg-latest.git`.
4. **Config Vars**:
   - Go to **'Settings'** -> **'Reveal Config Vars'**.
   - Add all variables listed in the Koyeb section above.
5. **Deployment Method**:
   - Go to **'Deploy'** tab.
   - Select **'GitHub'** and connect your forked repo.
   - Scroll down and click **'Deploy Branch'**.
6. **Resources**:
   - Once deployed, go to **'Resources'**.
   - Ensure the `web` dyno is turned **ON**.

---

## 💻 3. VPS DEPLOYMENT (Highest Performance)
The best method for large files and heavy media processing.

### Step-by-Step:
1. **Update & Install Dependencies**:
   ```bash
   sudo apt update && sudo apt upgrade -y
   sudo apt install git python3 python3-pip ffmpeg mkvtoolnix -y
   ```
2. **Clone the Repository**:
   ```bash
   git clone https://github.com/ALONEKINGSTAR77/WZML hemanth-bot
   cd hemanth-bot
   ```
3. **Install Requirements**:
   ```bash
   pip3 install -r requirements.txt
   ```
4. **Setup Environment Variables**:
   - Copy the sample file: `cp config_sample.env config.env`
   - Edit the file: `nano config.env`
   - Fill in your `BOT_TOKEN`, `OWNER_ID`, `TELEGRAM_API`, `TELEGRAM_HASH`, and `DATABASE_URL`.
   - Press `Ctrl+O` then `Enter` to save, and `Ctrl+X` to exit.
5. **Run the Bot**:
   - **Standard Run**: `python3 -m bot`
   - **Recommended Run (using screen)**:
     ```bash
     screen -S bot
     python3 -m bot
     ```
     *(Press `Ctrl+A+D` to detach and keep it running in background)*

---

## 🛠️ TROUBLESHOOTING
- **"Missing Token"**: Ensure `config.env` is correctly placed or environment variables are set in the dashboard.
- **Button not responding**: Check if the bot has admin rights in the log channel.
- **FFmpeg error**: Ensure you added the FFmpeg buildpack (Heroku) or installed it (VPS).

---

## 🤝 SUPPORT
Join our support group: [⚡𝗛𝗘𝗠𝗔𝗡𝗧𝗛⚡ Updates](https://t.me/ALONEKINGSTAR77)
Owner: [@ALONEKINGSTAR77](https://t.me/ALONEKINGSTAR77)
