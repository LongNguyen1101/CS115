import streamlit as st
import requests

# Tiêu đề ứng dụng
st.title("Translator App")

# Nhập văn bản từ người dùng
input_text = st.text_area("Enter text to translate:", "")

# Gửi yêu cầu tới API khi bấm nút
if st.button("Translate"):
    if input_text.strip():
        try:
            # Gọi API
            response = requests.post(
                "http://127.0.0.1:8000/translate", 
                json={"text": input_text}
            )
            # Kiểm tra phản hồi từ API
            if response.status_code == 200:
                translated_text = response.json().get('Translated text')
                st.success(f'{translated_text}')
            else:
                st.error(f"Error: {response.status_code} - {response.text}")
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
    else:
        st.warning("Please enter text to translate.")
