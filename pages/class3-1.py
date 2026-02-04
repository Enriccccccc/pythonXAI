import streamlit as st

st.title("🛒 購物籃系統（自動合併重複）")

# 初始化購物籃
if "cart" not in st.session_state:
    st.session_state.cart = {}


# 加入商品
def add_item():
    item = st.session_state.new_item.strip()
    if item:
        if item in st.session_state.cart:
            st.session_state.cart[item] += 1
        else:
            st.session_state.cart[item] = 1
        st.session_state.new_item = ""
    else:
        st.warning("商品名稱不能為空白！")


st.header("新增商品")

# 輸入框 + 按鈕
col1, col2 = st.columns([5, 1])

with col1:
    st.text_input(
        "商品名稱", key="new_item", label_visibility="collapsed", on_change=add_item
    )

with col2:
    if st.button("加入"):
        add_item()

st.header("購物籃內容")

# 清空購物籃
if st.button("清空購物籃"):
    st.session_state.cart.clear()
    st.rerun()

# 顯示內容
if not st.session_state.cart:
    st.info("購物籃目前是空的。")
else:
    for i, (name, qty) in enumerate(st.session_state.cart.items()):
        col1, col2 = st.columns([5, 1])
        col1.write(f"{name} x{qty}")
        if col2.button("刪除", key=f"del_{i}"):
            st.session_state.cart.pop(name)
            st.rerun()
