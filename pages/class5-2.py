from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

while True:
    user_input = input("you: ")

    if user_input.lower() in ["exit", "quit"]:
        break

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_input},
        ],
    )

    assistant_response = response.choices[0].message.content
    print("AI:", assistant_response)
