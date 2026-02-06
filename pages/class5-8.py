import streamlit as st
import openai
from utils import load_openai_api, encode_image

openai.api_key = load_openai_api()

st.title("AI pic analysis")

uploaded_file = st.file_uploader("Upload a file", type=["png", "jpg", "jpeg"])

assistant_response = None  # avoid undefined variable

if uploaded_file:
    st.image(uploaded_file, caption="Uploaded file", width=500)

    # save image temporarily
    with open("temp_image.jpg", "wb") as f:
        f.write(uploaded_file.getbuffer())

    base64_image = encode_image("temp_image.jpg")

    prompt = st.chat_input("pls enter prompt")

    if prompt:
        response = openai.chat.completions.create(
            model="gpt-5.1-chat-latest",  # ← EXACTLY as you want
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": prompt,
                        },
                        {
                            "type": "image_url",  # ← keep this
                            "image_url": {
                                "url": f"data:image/jpeg;base64,{base64_image}"
                            },
                        },
                    ],
                },
            ],
        )

        assistant_response = response.choices[0].message.content

if assistant_response:
    st.write(assistant_response)
