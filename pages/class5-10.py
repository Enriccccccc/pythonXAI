import streamlit as st
import openai
import base64
from utils import load_openai_api

openai.api_key = load_openai_api()

st.title("AI pic genrate")

st.header("use word to make pic")

size = st.selectbox(
    "圖像尺寸",
    ["1024x1024", "1536x1024", "1024x1536", "auto"],
    help="方形圖片生成速度最快，預設為 1024x1024 像素",
)

quality = st.selectbox(
    "圖像品質",
    ["auto", "low", "medium", "high"],
    help="high quality, long gnerate time, hight cost",
)

output_format = st.selectbox(
    "輸出格式",
    ["png", "jpg", "jpeg"],
    help="choose the output format",
)

background = st.selectbox(
    "background option",
    ["auto", "transparent]"],
    help="transparent background is only suitable for PNG and WebP",
)

if background == "transparent" and output_format != "jpeg":
    st.warning("transparent background is only suitable for PNG and WebP")

if output_format in ["jpeg", "webp"]:
    output_compression = st.slider(
        "壓縮率",
        min_value=0,
        max_value=100,
        value=75,
        help="壓縮率越高，圖像越小，但是圖像生成速度越慢",
    )

prompt_text = st.text_area("hint text")

moderation = st.selectbox(
    "審查嚴格度", ["auto", "low"], help="auto為標準過濾，low為低過濾"
)

if st.button("generate"):
    with st.spinner("Generating..."):
        try:
            params = {
                "model": "gpt-image-1.5",
                "prompt": prompt_text,
                "n": 1,
                "size": size,
                "quality": quality,
            }

            if background != "auto":
                params["background"] = background

            generatedImage = openai.images.generate(**params)

            image_base64 = generatedImage.data[0].b64_json
            image_bytes = base64.b64decode(image_base64)

            st.image(image_bytes)

            token_cost = {
                "1024x1024": {"low": 272, "medium": 1056, "high": 4160},
                "1024x1536": {"low": 408, "medium": 1584, "high": 6240},
                "1536x1024": {"low": 400, "medium": 1568, "high": 6208},
            }

            if quality != "auto" and size != "auto":
                try:
                    est_tokens = token_cost[size][quality]
                    st.info(f"預估使用約 {est_tokens} 個圖像 token，加上少量文字 token")
                except:
                    pass

            st.download_button(
                label="下載圖片",
                data=image_bytes,
                file_name=f"generated_image.{output_format}",
                mime=f"image/{output_format}",
            )

        except Exception as e:
            st.error(f"生成圖片時發生錯誤: {e}")
