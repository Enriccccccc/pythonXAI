import streamlit as st

st.title("排版練習")

(
    col1,
    col2,
) = st.columns(2)
if col1.button("balloon_button"):
    col1.balloons()
if col2.button("snow_button"):
    col2.snow()

col3, col4, col5 = st.columns([1, 2, 3])
with col3:
    st.write("at_col3")
    st.button("button3")
with col4:
    st.write("at_col4")
    st.button("button4")
with col5:
    st.write("at_col5")
    st.button("button5")

numCol = st.number_input("請輸入欄位數量", min_value=1, max_value=5, value=3, step=1)
numButton = st.number_input("請輸入按鈕數量", min_value=1, value=10, step=1)
cols = st.columns(numCol)
for i in range(numButton):
    cols[i % numCol].button(f"按鈕{i+1}")

st.title("文字輸入元件")
text = st.text_input("請輸入文字")
st.write("你輸入的文字是：" + text)
