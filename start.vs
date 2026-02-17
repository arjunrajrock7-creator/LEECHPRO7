#!/bin/bash

# Start aria2
chmod +x aria.vs
bash aria.vs

# Wait for aria2 RPC
echo "⏳ Waiting for Aria2 RPC to be ready on port 6800..."
MAX_RETRIES=30
RETRY_COUNT=0
while ! curl -s http://localhost:6800/jsonrpc > /dev/null; do
  RETRY_COUNT=$((RETRY_COUNT+1))
  if [ $RETRY_COUNT -ge $MAX_RETRIES ]; then
    echo "❌ Aria2 RPC failed to start after $MAX_RETRIES seconds!"
    exit 1
  fi
  sleep 1
done
echo "✅ Aria2 RPC is ready!"

# Run validation and start bot
python3 validate.py && python3 update.py && python3 -m bot
