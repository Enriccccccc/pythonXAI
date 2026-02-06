import streamlit as st

st.title("這是首頁")

st.set_page_config(page_title="my first web app", page_icon="🏠", layout="wide")

# streamlit run main.py

all_pages = {
    "": [
        st.Page("pages/hand_book.py", title="課程筆記", icon="📖"),
    ],
    "📚 程式練習": [
        st.Page("pages/class1-2.py", title="Markdown語法", icon="📝"),
        st.Page("pages/class2-1.py", title="成績等第判斷", icon="📊"),
        st.Page("pages/class2-3.py", title="金字塔系列", icon="🔺"),
        st.Page("pages/class2-7.py", title="排版練習", icon="🖍️"),
        st.Page("pages/class3-1.py", title="點餐機", icon="🍽️"),
        st.Page("pages/class3-5.py", title="guess the number", icon="🎲"),
        st.Page("pages/class4-1.py", title="pic", icon="📸"),
        st.Page("pages/class4-2.py", title="shopping", icon="🛒"),
        st.Page("pages/class5-4.py", title="chat", icon="😊"),
        st.Page("pages/class5-5.py", title="type chat", icon="😊"),
        st.Page("pages/class5-6.py", title="AI chat", icon="😊"),
        st.Page("pages/class5-7.py", title="pic upload", icon="😊"),
        st.Page("pages/class5-8.py", title="ai pic analysis", icon="😊"),
        st.Page("pages/class5-9.py", title="website loading", icon="⌛"),
        st.Page("pages/class5-10.py", title="website loading", icon="⌛"),
    ],
}

nav = st.navigation(all_pages, position="sidebar")
nav.run()
