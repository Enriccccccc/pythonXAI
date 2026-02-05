import streamlit as st
import os
import time

st.title("圖片元件")

st.image("image/hamster staring.jpg", width=300, caption="hamster")
st.image("image/cojo.jpg", width=300, caption="cojo")

image_folder = "image"
image_files = os.listdir(image_folder)
image_files.sort()
st.write(image_files)

for image_file in image_files:
    image_path = image_folder + "/" + image_file
    st.image(image_path, width=300)

for image_file in image_files:
    image_path = image_folder + "/" + image_file
    st.image(image_path, use_container_width=True)

st.title("select box component")

selected_images = st.selectbox("choose images", image_files)
st.write("selected_images:", selected_images[:-4])
image_path = image_folder + "/" + selected_images
st.image(image_path, width=500)

st.title("website message component")

cols = st.columns(4)

# success
if cols[0].button("success button"):
    st.success("this is st.succes message")
    time.sleep(1)
    st.rerun()

# error
if cols[1].button("error button"):
    st.error("this is st.error message")
    time.sleep(1)
    st.rerun()
# warning
if cols[2].button("warning button"):
    st.warning("this is st.warning message")
    time.sleep(1)
    st.rerun()
# info
if cols[3].button("info button"):
    st.info("this is st.info message")
    time.sleep(1)
    st.rerun()
