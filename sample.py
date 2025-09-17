import streamlit as st
from PIL import Image
import pytesseract

st.set_page_config(page_title="Tesseract OCR App", page_icon="📄", layout="centered")

st.title("📄 OCR with Tesseract + Streamlit")

# File uploader
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    if st.button("Extract Text"):
        with st.spinner("Running OCR..."):
            text = pytesseract.image_to_string(image)

        st.subheader("📜 Extracted Text:")
        st.text_area("Output", text, height=200)

        # Option to download the text
        st.download_button(
            label="Download Text",
            data=text,
            file_name="ocr_output.txt",
            mime="text/plain"
        )
