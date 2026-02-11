# ⚡𝗛𝗘𝗠𝗔𝗡𝗧𝗛⚡ Mirror-Leech Bot

A powerful Telegram Mirror-Leech Bot based on WZML-X, optimized for Koyeb, Heroku, and VPS deployment.

## ☘️ FEATURES ☘️
- Mirror direct links, torrents, and media to Google Drive, RClone, or DDL servers.
- Leech to Telegram with custom settings.
- **Video Tools Suite:**
  - Metadata Editor (Global/Task)
  - Track Selection (Audio/Subtitle)
  - Video Compressor (Custom Bitrate)
  - Video Merger (Auto/Manual)
  - Watermark (Image/Text)
  - Subtitle Synchronization
- Custom Progress Bar: 🟥🟥⬜
- Stylized UI Theme with math fonts and emojis.
- Highly optimized for Koyeb (100% Success Rate).

## 🚀 DEPLOYMENT 🚀

### ☁️ Koyeb
1. Fork this repository.
2. Create a new App on Koyeb.
3. Choose "Web Service".
4. Select your forked repo.
5. In the Build Command, enter: `pip3 install -r requirements.txt` (or leave as default if using Docker).
6. In the Run Command, enter: `python3 -m bot` (or leave as default if using Docker).
7. Add your Environment Variables from `config.env`.
8. Deploy!

### 💜 Heroku
1. Fork this repository.
2. Create a new App on Heroku.
3. Add the Python Buildpack.
4. Add the FFmpeg and Rclone Buildpacks.
5. Connect your GitHub and Deploy.
6. The `Procfile` is already included.

### 💻 VPS / Local
1. `git clone https://github.com/ALONEKINGSTAR77/WZML`
2. `cd WZML`
3. `pip3 install -r requirements.txt`
4. Fill `config.env`.
5. `python3 -m bot`

## 🛠 VARIABLES 🛠
- `API_ID`: Your Telegram API ID.
- `API_HASH`: Your Telegram API HASH.
- `BOT_TOKEN`: Your Telegram Bot Token.
- `OWNER_ID`: Your Telegram User ID.
- `DATABASE_URL`: Your MongoDB Connection String.
- `LOG_CHANNEL_ID`: Channel ID for logs.

## 🤝 SUPPORT 🤝
Join our support group: [⚡𝗛𝗘𝗠𝗔𝗡𝗧𝗛⚡ Updates](https://t.me/ALONEKINGSTAR77)
Owner: [@ALONEKINGSTAR77](https://t.me/ALONEKINGSTAR77)

## 📜 LICENSE 📜
This project is licensed under the MIT License.
