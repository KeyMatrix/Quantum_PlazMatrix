
import streamlit as st
import json
import time
import requests

with open("meta_bridge_config.json") as f:
    config = json.load(f)

st.set_page_config(page_title="MetaBridge Dashboard", layout="wide")
st.title("🧠 MetaBridge.om Dashboard")
st.markdown("#### Режим наблюдения за мостом между измерениями")

st.sidebar.header("Настройки соединений")
st.sidebar.write(f"🔗 GitHub: {config['github_repo']}")
st.sidebar.write(f"🌐 Discord Webhook: {config['discord_webhook_url']}")
st.sidebar.write(f"🔧 Sync Level: {config['sync_level']}")

st.markdown("### 🧩 Активные модули")
for module in config["meta_settings"]["modules_active"]:
    st.success(f"✅ {module}")

st.markdown("### 📡 Последние сигналы Discord")
log_placeholder = st.empty()

def poll_discord():
    try:
        log_placeholder.markdown(f"📥 `MetaBridge Active | Time: {time.strftime('%H:%M:%S')}`")
    except Exception as e:
        log_placeholder.error(f"Ошибка связи: {e}")

refresh = st.checkbox("Автообновление", value=True)
while refresh:
    poll_discord()
    time.sleep(5)
