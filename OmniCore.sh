#!/bin/bash

echo "🔹 [1] Установка зависимостей для Python..."
if [ -f "requirements.txt" ]; then
    pip install -r requirements.txt || pip3 install -r requirements.txt
else
    echo "⚠️ Файл requirements.txt не найден. Создаю..."
    echo -e "requests\nwebsocket-client" > requirements.txt
    pip install -r requirements.txt || pip3 install -r requirements.txt
fi

echo "🔸 [2] Установка зависимостей для Node.js..."
if [ -f "package.json" ]; then
    npm install
else
    echo "⚠️ Файл package.json не найден. Проверь наличие Node.js зависимостей."
fi

echo "🌀 [3] Запуск TreeOM AppServer..."
python3 TreeOM_AppServer.py &

echo "🌐 [4] Запуск WebSocket-сервера..."
node websocket_server.js &

echo "💎 [5] Запуск Discord-интеграции..."
node discord_bot.js &

echo "🧠 [6] Запуск Live Web-интерфейса..."
npx live-server --port=8080 &

sleep 2
echo "🛠️ [7] Запуск мониторинга структуры..."
python3 treeom_monitor.py &

sleep 2
echo "📦 [8] Проверка CI/CD pipeline..."
if [ -f .github/workflows/main.yml ]; then
    echo "✔️ GitHub Actions workflow найден."
else
    echo "⚠️ Workflow не найден! Создаю шаблон..."
    mkdir -p .github/workflows
    cp ./templates/ci_template.yml .github/workflows/main.yml
fi

echo "📘 [9] Обновление README.md..."
if ! grep -q "MetaForge" README.md; then
    echo "## MetaForge Activated" >> README.md
    echo "- Автоматическое обновление конфигураций." >> README.md
fi

echo "✅ Все потоки активированы. MetaForge в резонансе."