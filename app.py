import streamlit as st

# Tiêu đề ứng dụng
st.title("Streamlit Cloud Test App")

# Nội dung chính
st.write("Chào mừng bạn đến với ứng dụng Streamlit của tôi!")

# Thêm một thành phần tương tác
name = st.text_input("Nhập tên của bạn:")
if st.button("Gửi"):
    st.write(f"Xin chào, {name}! Bạn đã kết nối thành công với Streamlit Cloud.")
