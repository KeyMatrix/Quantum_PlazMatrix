#!/bin/bash

echo "🔹 [MetaForge] Initializing OmniSync Core..."
python3 TreeOM_AppServer.py &

sleep 2
echo "🔸 [MetaForge] Starting WebSocket Interface..."
node websocket_server.js &

sleep 2
echo "🌀 [MetaForge] Launching Discord Integration..."
node discord_bot.js &

sleep 2
echo "💎 [MetaForge] Live Interface ready on port 8080."
npx live-server --port=8080 &

echo "🫂 All systems connected. MetaForge resonance online."