import streamlit as st

st.chat_message("user").write("this is user message")
st.chat_message("assistant").write("this is assistant message")

# chatting history example
history = [
    {"role": "user", "content": "hello AI"},
    {"role": "assistant", "content": " hello, wut can i do for you?"},
    {"role": "user", "content": "how to use st.chat_message()"},
    {
        "role": "assistant",
        "content": "st.chat_message() i can let u use chatting box to show message!",
    },
]

# using loop to show chatting history
for message in history:
    if message["role"] == "user":
        st.chat_message("user", avatar="😊").write(message["content"])
    else:
        st.chat_message("assistant", avatar="👽").write(message["content"])
