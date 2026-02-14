import os
import sys
import asyncio
from pyrogram import Client

async def validate():
    print("🚀 Starting Pre-Startup Validation...")

    # 1. Check for config.env
    if not os.path.exists("config.env"):
        print("❌ Error: config.env not found!")
        sys.exit(1)

    # 2. Basic ENV validation
    required = ["BOT_TOKEN", "OWNER_ID", "TELEGRAM_API", "TELEGRAM_HASH"]
    from dotenv import load_dotenv
    load_dotenv("config.env")

    for key in required:
        if not os.environ.get(key):
            print(f"❌ Error: {key} is missing in config.env!")
            sys.exit(1)

    # 3. Token validation
    token = os.environ.get("BOT_TOKEN")
    api_id = os.environ.get("TELEGRAM_API")
    api_hash = os.environ.get("TELEGRAM_HASH")

    print("📡 Validating BOT_TOKEN...")
    try:
        async with Client("validate_session", api_id=api_id, api_hash=api_hash, bot_token=token, in_memory=True) as app:
            me = await app.get_me()
            print(f"✅ Bot Token is Valid! (Bot: @{me.username})")
    except Exception as e:
        print(f"❌ Error: Bot Token or API Credentials invalid! ({e})")
        sys.exit(1)

    print("✅ All Pre-Startup checks passed!")

if __name__ == "__main__":
    asyncio.run(validate())
