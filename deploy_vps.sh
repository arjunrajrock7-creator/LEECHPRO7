#!/bin/bash

# ⚡𝗛𝗘𝗠𝗔𝗡𝗧𝗛⚡ Bot VPS Auto-Deploy Script
# Suitable for DaRemote and Mobile SSH Clients

echo "🚀 Starting Deployment of ⚡𝗛𝗘𝗠𝗔𝗡𝗧𝗛⚡ Bot..."

# Update and install dependencies
sudo apt-get update && sudo apt-get upgrade -y
sudo apt-get install -y git docker.io docker-compose curl

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
