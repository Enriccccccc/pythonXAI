import streamlit as st

st.title("數字輸入練習")
number = st.number_input("請輸入一個數字", min_value=0, max_value=100, value=50, step=5)
st.write(f"你輸入的數字是: {number}")

st.title("成績等級判斷")
score = st.number_input("請輸入你的成績", min_value=0, max_value=100, value=75, step=1)
if score >= 90:
    st.write("成績等級: A")
elif score >= 80:
    st.write("成績等級: B")
elif score >= 70:
    st.write("成績等級: C")
elif score >= 60:
    st.write("成績等級: D")
else:
    st.write("成績等級: F")

st.title("氣球按鈕")
if st.button("點我", key="balloon_button"):
    st.balloons()

st.title("下雪按鈕")
if st.button("下雪", key="snow_button"):
    st.snow()
