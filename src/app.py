import streamlit as st
from src.data_handler import DataHandler
import base64
from io import BytesIO

# TODO properly build out the persona templates and storage
persona = ["Eris Bloom", "src/static/images/Eris0001.png"]


def set_page_config(
    page_title="Eris MischiefBloom",
    page_icon="🌺",
    layout="wide",
    initial_sidebar_state="expanded",
):
    st.set_page_config(
        page_title=page_title,
        page_icon=page_icon,
        layout=layout,
        initial_sidebar_state=initial_sidebar_state,
    )


st.title(persona[0])

data_handler: DataHandler = DataHandler(persona[1])

blob_link: str = data_handler.handle_image()

image = BytesIO(base64.b64decode(blob_link))

with st.sidebar:
    st.image(image)
    with st.container():
        st.markdown("")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("prompt"):
    state_message = st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )
    with st.chat_message("user"):
        st.markdown(prompt)

if prompt is not None:
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        for response in data_handler.handle_chat(content=prompt, role="user"):
            full_response += response.choices[0].delta.get("content", "")
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)
        message = {"role": "assistant", "content": full_response}
    data_handler.handle_ai_chat(message)
    state_message = st.session_state.messages.append(message)
