import streamlit as st
import os

st.title("hand_book")

folder_path = "markdown"
files = os.listdir(folder_path)
files.sort()
selected_files = []
for file in files:
    if file.endswith(".md"):
        with st.expander(file[:-3]):
            file_path = folder_path + "/" + file
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
                st.write(content)


for file in selected_files:
    with st.expander(file):
        file_path = folder_path + "/" + file + ".md"
