import streamlit as st

uploaded_file = st.file_uploader("Upload a file", type=["png", "jpg", "jpeg"])

if uploaded_file:
    st.image(uploaded_file, caption="Uploaded file", width=500)
