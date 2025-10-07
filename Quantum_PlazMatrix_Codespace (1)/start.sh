#!/bin/bash
echo "🔹 Запуск OmniSync Core12..."
node websocket_server.js &

echo "🔸 Запуск Discord Bot..."
node discord_bot.js &

echo "🌀 Готово. Открой web_interface.html в Codespace Preview."
