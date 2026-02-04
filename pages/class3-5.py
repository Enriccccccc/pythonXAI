import random
import streamlit as st
import time

ss = st.session_state

# initialize
if "target" not in ss:
    ss.target = random.randint(0, 100)

if "min_val" not in ss:
    ss.min_val = 0

if "max_val" not in ss:
    ss.max_val = 100


def guess():
    num = ss.user_num
    if num < ss.target:
        st.success("bigger")
        ss.min_val = num + 1
    elif num > ss.target:
        st.success("smaller")
        ss.max_val = num - 1
    else:
        st.success("goody boi, u did it")
        st.balloons()
        ss.target = random.randint(0, 100)
        ss.min_val = 0
        ss.max_val = 100
    time.sleep(1)
    st.rerun()


st.title("猜數字")

st.number_input(
    f"請輸入一個 {ss.min_val} 到 {ss.max_val} 的數字",
    min_value=ss.min_val,
    max_value=ss.max_val,
    step=1,
    key="user_num",
    on_change=guess,  # 按 Enter 會自動猜
)

if st.button("猜"):
    guess()
