import streamlit as st

ss = st.session_state

st.title("session_state_example")

if "ans" not in ss:
    ss.ans = 0

if st.button("click me to +1"):
    ss.ans += 1
    st.rerun()

st.write("ans=", ss.ans)
