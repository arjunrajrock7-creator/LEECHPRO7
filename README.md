<p align="center">
    <img src="https://graph.org/file/639fe4239b78e5862b302.jpg" alt="WZML-X Logo" width="200">
</p>

<h1 align="center">🚀 WZML-X: The Ultimate Mirror-Leech Bot</h1>

<p align="center">
    <i>A high-performance Telegram bot built with Pyrogram for all your mirroring, leeching, and cloning needs.</i>
</p>

<p align="center">
    <a href="https://github.com/weebzone/WZML-X/stargazers"><img src="https://img.shields.io/github/stars/weebzone/WZML-X?style=for-the-badge&color=yellow" alt="Stars"></a>
    <a href="https://github.com/weebzone/WZML-X/network/members"><img src="https://img.shields.io/github/forks/weebzone/WZML-X?style=for-the-badge&color=blue" alt="Forks"></a>
    <a href="https://github.com/weebzone/WZML-X/blob/master/LICENSE"><img src="https://img.shields.io/github/license/weebzone/WZML-X?style=for-the-badge&color=green" alt="License"></a>
    <a href="https://t.me/WZML_X"><img src="https://img.shields.io/badge/Telegram-Channel-blue?style=for-the-badge&logo=telegram" alt="Telegram Channel"></a>
</p>

---

## ✨ Key Features

- **Multi-Engine Support**: Integrated with Aria2c, qBittorrent, and YT-DLP.
- **Versatile Mirroring**: Mirror links, files, and magnets to Google Drive, RClone-supported clouds, or DDL servers.
- **Leech Capabilities**: Upload files to Telegram with custom thumbnails, captions, and automatic splitting.
- **Premium Merge**: Automatically merge multiple video files into a single high-quality MKV file.
- **Metadata Integration**: Add custom metadata to your leeched videos.
- **Premium UI**: Experience a stylized interface with math alphanumeric fonts, custom emojis, and hexagon-style progress bars.
- **Database Backed**: Persistent settings, RSS feeds, and task history using MongoDB.
- **Multi-User Ready**: Individual settings for users, including custom TD, RClone config, and more.

---

## 🛠 Deployment Guides

### 🚀 Koyeb (Recommended)

<details>
  <summary><b>Click for Koyeb Step-by-Step Guide</b></summary>

1. **Fork the Repo**: Fork this repository to your GitHub account.
2. **Setup Credentials**: Edit `config.env` in your fork or set them as Environment Variables in Koyeb.
   - `BOT_TOKEN`, `OWNER_ID`, `TELEGRAM_API`, `TELEGRAM_HASH`, `DATABASE_URL`.
3. **Deploy on Koyeb**:
   - Create a new **Service** and select **GitHub**.
   - Use the **Docker** builder.
   - **Health Check**: Set to `HTTP`, Port `8000`, Path `/`.
4. **Launch**: Click Deploy and wait for the magic!

</details>

### 🐳 Docker (Local/VPS)

```bash
git clone https://github.com/weebzone/WZML-X wzmlx && cd wzmlx
cp config_sample.env config.env
# Edit config.env with your values
docker compose up -d
```

---

## 🤖 Bot Commands

| Command | Description |
| :--- | :--- |
| `/mirror` | Mirror links/files to Cloud |
| `/leech` | Leech links/files to Telegram |
| `/qbmirror` | Mirror via qBittorrent |
| `/ytdl` | Mirror via YT-DLP |
| `/usetting` | Personal settings & Merge toggle |
| `/bsetting` | Global bot settings (Sudo only) |
| `/status` | View active tasks |
| `/cancel` | Stop a running task |

---

## 📝 Configuration Variables

| Variable | Description |
| :--- | :--- |
| `BOT_TOKEN` | Your Telegram Bot Token from @BotFather |
| `OWNER_ID` | Your Telegram User ID |
| `TELEGRAM_API` | API ID from my.telegram.org |
| `TELEGRAM_HASH` | API HASH from my.telegram.org |
| `DATABASE_URL` | MongoDB Connection String |
| `LEECH_MERGE` | Default status for video merging (True/False) |

---

## 🤝 Credits

- [SilentDemonSD](https://github.com/SilentDemonSD) - Lead Developer
- [CodeWithWeeb](https://github.com/weebzone) - Contributor
- [Maverick](https://github.com/MajnuRangeela) - Bug Tester

---

<p align="center">
    Made with ❤️ by <a href="https://github.com/weebzone">WeebZone</a>
</p>
