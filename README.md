<p align="center">
    <img src="https://graph.org/file/639fe4239b78e5862b302.jpg" alt="⚡𝗛𝗘𝗠𝗔𝗡𝗧𝗛⚡ Logo" width="200">
</p>

<h1 align="center">⚡𝗛𝗘𝗠𝗔𝗡𝗧𝗛⚡: Production-Grade Mirror-Leech Bot</h1>

<p align="center">
    <i>A high-performance, stable, and feature-rich Telegram bot for professional mirroring, leeching, and media processing.</i>
</p>

<p align="center">
    <a href="https://t.me/ALONEKINGSTAR77"><img src="https://img.shields.io/badge/Telegram-Channel-blue?style=for-the-badge&logo=telegram" alt="Telegram Channel"></a>
    <a href="https://t.me/ALONEKINGSTAR77"><img src="https://img.shields.io/badge/Support-Group-red?style=for-the-badge&logo=telegram" alt="Support Group"></a>
</p>

---

## ✨ Advanced Features

### 🚀 Performance & Stability
- **Async Queue System**: Robust handling of multiple tasks with priority and state tracking.
- **Production UI**: Zero loading loops, responsive buttons, and instant callback handling.
- **Low RAM Usage**: Optimized for large file handling without memory leaks.
- **Koyeb Optimized**: 100% stable deployment with built-in health checks.

### 📦 FFmpeg Media Suite
- **Metadata Editor**: Edit title, artist, language, and encoder details.
- **Track Manager**: Selectively keep/remove audio and subtitle tracks.
- **Compressor**: Presets for low/medium/high/custom bitrates.
- **Video Tools**: Generate samples, trim videos, and extract high-quality thumbnails.
- **Merge Features**: "Merge + Original" toggle to keep source files while generating MKVs.

### ☁️ Mirroring & Leeching
- **Multi-Engine**: Supports Aria2c, qBittorrent, and YT-DLP.
- **Cloud Support**: GDrive, RClone, and various DDL servers.
- **Customization**: Custom thumbnails, captions (with templates), and split sizes.

---

## 🛠 Deployment Guides

### 🚀 Koyeb (Recommended)

1. **Fork the Repo**: Click the fork button to get your own copy.
2. **Setup config.env**: Create a `config.env` file or set variables in Koyeb.
3. **Deploy**:
   - Create a new Service on Koyeb.
   - Select **Docker** builder.
   - Set **Health Check** to `HTTP`, Port `8000`, Path `/health`.
4. **Environment**: Add all required variables (see below).

### 🐳 Docker (Self-Hosted)

```bash
git clone https://t.me/ALONEKINGSTAR77 && cd ⚡𝗛𝗘𝗠𝗔𝗡𝗧𝗛⚡
# Edit config.env
docker compose up -d
```

---

## 📝 Environment Variables

| Variable | Description |
| :--- | :--- |
| `BOT_TOKEN` | Telegram Bot Token from @BotFather |
| `OWNER_ID` | Your Telegram User ID |
| `TELEGRAM_API` | API ID from my.telegram.org |
| `TELEGRAM_HASH` | API HASH from my.telegram.org |
| `DATABASE_URL` | MongoDB Connection URL |
| `LEECH_MERGE` | Enable/Disable video merging (True/False) |
| `PORT` | Web server port for health checks (Default: 8000) |

---

## 🤖 Bot Commands

- `/mirror`: Mirror links/files to Cloud.
- `/leech`: Leech files to Telegram.
- `/usetting`: Open user-specific settings and toggles.
- `/bsetting`: Global bot settings (Sudo only).
- `/status`: View active tasks and system stats.
- `/cancel`: Stop a running task.

---

## 🔧 Troubleshooting

- **Button not responding?**: Ensure you are using the latest version with the `@callback_handler` fix.
- **Deployment failing?**: Check Koyeb logs. Ensure `PORT` is correctly set and `gunicorn` is running.
- **Large files stuck?**: Check your split size settings in `/usetting`.

---

<p align="center">
    Developed with ❤️ by <a href="https://t.me/ALONEKINGSTAR77">⚡𝗛𝗘𝗠𝗔𝗡𝗧𝗛⚡</a>
</p>
