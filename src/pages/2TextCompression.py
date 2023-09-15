import streamlit as st
from compression_request import requestion_text_compression

st.title("Text Compression")
main_container = st.container()
sidebar_container = st.sidebar

with sidebar_container:
    st.file_uploader("Upload your data")
    st.text_input("or Enter stored file name")
