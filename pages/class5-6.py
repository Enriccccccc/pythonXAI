from openai import OpenAI
import streamlit as st
from utils import load_openai_api

ss = st.session_state

client = OpenAI(api_key=load_openai_api())

if "history" not in ss:
    ss.history = []

if "system_message" not in ss:
    ss.system_message = "use english to chat."

if "model" not in ss:
    ss.model = "gpt-4.1-mini"

col1, col2, col3 = st.columns([4, 2, 1])
with col1:
    ss.system_message = st.text_input("system message", ss.system_message)

with col2:
    ss.model = st.selectbox(
        "AI Model",
        [
            "gpt-5.1-chat-latest",
            "gpt-5.1",
            "gpt-5",
        ],
    )

with col3:
    if st.button("🗑️"):
        ss.history = []
        st.rerun()

# 顯示歷史對話
for message in ss.history:
    st.chat_message(message["role"]).write(message["content"])

prompt = st.chat_input("請輸入問題：")

if prompt:
    ss.history.append({"role": "user", "content": prompt})

    # ⭐ 正確的 OpenAI API 語法
    response = client.chat.completions.create(
        model=ss.model,
        messages=[{"role": "system", "content": ss.system_message}] + ss.history,
    )

    reply = response.choices[0].message.content
    ss.history.append({"role": "assistant", "content": reply})

    st.rerun()
