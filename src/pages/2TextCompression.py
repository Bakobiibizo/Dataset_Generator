import streamlit as st
from request_compression import requestion_text_compression

st.title("Text Compression")
main_container = st.container()
sidebar_container = st.sidebar

with sidebar_container:
    data = st.file_uploader("Upload your data")
    filename = st.text_input("or Enter stored file name")
    submit_button = st.button("Submit")

if submit_button:
    compressed_transcripts, file_name = requestion_text_compression(data)
    with main_container:
        st.markdown(compressed_transcripts)
        st.markdown(f"File name: {file_name}")
        st.download_button("Download", compressed_transcripts, file_name)
