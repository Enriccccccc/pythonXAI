import streamlit as st

st.title("數字金字塔")
# type a number pyramid
pyramid = st.number_input("請輸入一個number", min_value=0, max_value=9, value=5, step=1)
st.title("數字金字塔:")
for i in range(1, pyramid + 1):
    st.write(" " * (pyramid - i) + str(i) * (2 * i - 1))

import streamlit as st

st.title("箭頭形狀")


def arrow_shape(height, shaft_height=4):
    output = ""
    # 上方尖頭
    for i in range(1, height + 1):
        spaces = " " * (height - i)
        stars = "*" * (2 * i - 1)
        output += spaces + stars + "\n"

    # 下方箭身（細直柱）
    shaft_spaces = " " * (height - 1)
    for _ in range(shaft_height):
        output += shaft_spaces + "*\n"

    return output


height = st.number_input("請輸入箭頭尖端高度：", min_value=1, value=5)
shaft_height = st.number_input("請輸入箭身高度：", min_value=1, value=4)

st.code(arrow_shape(int(height), int(shaft_height)))
