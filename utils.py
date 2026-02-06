import streamlit as st
import base64


def load_openai_api() -> str:
    openai_api_key = st.secrets["OPENAI_API_KEY"]
    if not openai_api_key:
        st.error("can't find openai api key")
        st.stop()
    return openai_api_key


def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")
