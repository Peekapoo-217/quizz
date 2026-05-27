import streamlit as st
import streamlit.components.v1 as components

# Cài đặt cấu hình trang Streamlit
st.set_page_config(
    page_title="England Quiz Game",
    page_icon="🇬🇧",
    layout="wide"
)

# Đọc nội dung file HTML
with open("index.html", "r", encoding="utf-8") as f:
    html_code = f.read()

# Hiển thị HTML lên Streamlit
# Set height đủ lớn để game không bị cắt mất giao diện (scrollbar)
components.html(html_code, height=900, scrolling=True)