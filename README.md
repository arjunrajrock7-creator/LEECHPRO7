# ⚡𝗛𝗘𝗠𝗔𝗡𝗧𝗛⚡ PREMIUM Mirror-Leech Bot

A high-performance, async-driven Telegram Mirror-Leech Bot optimized for Koyeb, VPS, and Heroku. Featuring a powerful Video Tools Engine and automated processing pipelines.

## ☘️ PREMIUM FEATURES ☘️
- **Advanced Video Tools Engine:**
  - Metadata Editor (Global/Task-level)
  - Audio Track Manager (Remove, Swap, Reorder)
  - Subtitle Manager (Remove, Sync, Reorder)
  - Video Compressor (Custom Bitrate, Ultrafast encoding)
  - Watermark Injection (Image/Text)
  - Intro Video Injection (Prepend segments)
  - MKV Attachment Manager (Add/Remove files)
- **Automated ZIP Pipeline:**
  - Auto Download → Extract → Process (Metadata/Tools) → Sequence Merge → Upload.
- **Performance Optimization:**
  - Async task management with priority queue.
  - CPU Thread Auto-Detection (Optimized for Koyeb).
  - Watchdog System to prevent stuck FFmpeg tasks.
- **Premium UI:**
  - Icon-based modern inline menus.
  - Zero-delay button responses.
  - Animated progress bars (🟥🟥⬜).

## 🚀 KOYEB DEPLOYMENT (ZERO FREEZING) 🚀
1. Fork this repository.
2. Create a "Web Service" on Koyeb.
3. Set **Build Command**: `pip3 install -r requirements.txt`.
4. Set **Run Command**: `python3 -m bot`.
5. **Environment Variables**:
   - Add all credentials from `config_sample.env`.
   - Set `FFMPEG_THREADS` to `1` or `2` for small instances to prevent freezing.
6. The bot includes a built-in health check and watchdog to ensure 100% uptime.

## 💻 VPS STEP-BY-STEP GUIDE (ERROR-FREE) 💻
1. **Update System**:
   ```bash
   sudo apt update && sudo apt upgrade -y
   ```
2. **Install Dependencies**:
   ```bash
   sudo apt install git python3 python3-pip ffmpeg mkvtoolnix -y
   ```
3. **Clone & Setup**:
   ```bash
   git clone https://github.com/ALONEKINGSTAR77/WZML hemanth-bot
   cd hemanth-bot
   pip3 install -r requirements.txt
   ```
4. **Configuration**:
   - Rename `config_sample.env` to `config.env`.
   - Fill in your variables (API_ID, BOT_TOKEN, etc.).
5. **Run**:
   ```bash
   python3 -m bot
   ```
   *(Recommended: Use `tmux` or `pm2` for long-running sessions)*

## 🛠 ADVANCED VARIABLES 🛠
- `FFMPEG_THREADS`: Number of CPU threads FFmpeg should use. Leave empty for auto-detection.
- `FFMPEG_TIMEOUT`: Max time (seconds) for an encoding task. Default is 7200.
- `auto_merge_zip`: Toggle this in User Settings to enable the ZIP pipeline automation.

## 🤝 SUPPORT 🤝
Join our support group: [⚡𝗛𝗘𝗠𝗔𝗡𝗧𝗛⚡ Updates](https://t.me/ALONEKINGSTAR77)
Owner: [@ALONEKINGSTAR77](https://t.me/ALONEKINGSTAR77)

## 📜 LICENSE 📜
MIT License. Optimized for high-speed operation and stability.
