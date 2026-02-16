#!/bin/bash

# ⚡𝗛𝗘𝗠𝗔𝗡𝗧𝗛⚡ Bot VPS Auto-Deploy Script
# Suitable for DaRemote and Mobile SSH Clients

echo "🚀 Starting Deployment of ⚡𝗛𝗘𝗠𝗔𝗡𝗧𝗛⚡ Bot..."

# Update and install dependencies
sudo apt-get update && sudo apt-get upgrade -y
sudo apt-get install -y git docker.io docker-compose curl

# Performance Tweaks for High-Speed Downloads/Uploads
echo "🚀 Applying system optimizations for Ultra Speed..."
sudo sysctl -w net.core.rmem_max=16777216
sudo sysctl -w net.core.wmem_max=16777216
sudo sysctl -w net.ipv4.tcp_rmem='4096 87380 16777216'
sudo sysctl -w net.ipv4.tcp_wmem='4096 65536 16777216'
sudo sysctl -w net.ipv4.tcp_congestion_control=bbr
sudo sysctl -w net.core.netdev_max_backlog=5000
sudo sysctl -w net.ipv4.tcp_max_syn_backlog=10000
sudo sysctl -w net.ipv4.tcp_slow_start_after_idle=0
sudo sysctl -w net.ipv4.tcp_tw_reuse=1
sudo sysctl -w fs.file-max=1000000

# Increase File Descriptor Limits
if ! grep -q "soft nofile 1000000" /etc/security/limits.conf; then
    echo "* soft nofile 1000000" | sudo tee -a /etc/security/limits.conf
    echo "* hard nofile 1000000" | sudo tee -a /etc/security/limits.conf
fi

# Stop existing containers if any
docker-compose down || true

# Check if directory exists, if not clone
if [ ! -d "WZML-X" ]; then
    echo "📥 Cloning repository..."
    git clone https://github.com/ALONEKINGSTAR77/WZML-X.git
    cd WZML-X
else
    cd WZML-X
    echo "🔄 Pulling latest changes..."
    git pull
fi

# Ensure config.env exists
if [ ! -f "config.env" ]; then
    echo "⚠️ config.env not found!"
    echo "‼️ PLEASE CREATE config.env WITH YOUR CREDENTIALS ‼️"
    exit 1
fi

# Build and Start
echo "🏗️ Building and starting the bot..."
docker-compose up --build -d

echo "✅ Deployment Successful!"
echo "📡 Bot is running in the background."
echo "📜 Use 'docker logs -f wzmlx_bot' to see logs."
