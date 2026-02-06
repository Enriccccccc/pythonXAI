from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# ⭐ 對話記憶在這裡
messages = [{"role": "system", "content": "You are a helpful assistant."}]

print("AI 已啟動，輸入 quit 離開。\n")

while True:
    user_input = input("You: ")

    if user_input.lower() in ["exit", "quit"]:
        break

    # ⭐ 把使用者訊息加入記憶
    messages.append({"role": "user", "content": user_input})

    # ⭐ 送出整段對話，讓 AI 記住之前的內容
    response = client.chat.completions.create(model="gpt-4.1-mini", messages=messages)

    ai_reply = response.choices[0].message.content
    print("AI:", ai_reply)

    # ⭐ 把 AI 的回覆也加入記憶
    messages.append({"role": "assistant", "content": ai_reply})
