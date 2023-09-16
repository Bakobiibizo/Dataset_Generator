import json
import streamlit as st
import requests
import loguru
from PIL import Image
import io
from data_models import Message
from typing import List, Tuple
from request_persona import (
    get_persona_map,
    get_persona_index,
    get_persona,
    get_persona_image,
)

logger = loguru.logger

API_URL = "http://localhost:8000/"

bundle = get_persona()


def change_session_state(bundle: Tuple[str, str, str, str]):
    persona_name, persona_image, persona_description, persona_icon = bundle
    if persona_name not in st.session_state:
        st.session_state["persona_name"] = persona_name
    if persona_image not in st.session_state:
        st.session_state["persona_image"] = persona_image
    if persona_description not in st.session_state:
        st.session_state["persona_description"] = persona_description
    if persona_icon not in st.session_state:
        st.session_state["persona_icon"] = persona_icon
    return bundle


def process_image(persona_img: str):
    # logger.info(persona_img)
    image_data = get_persona_image(persona_img)
    image_stream = io.BytesIO(image_data)
    return Image.open(image_stream)


def get_maps():
    persona_indx = get_persona_index().decode("utf-8")
    persona_mp = get_persona_map().decode("utf-8")
    # logger.info(f"{persona_indx}\n{persona_mp}")
    return persona_indx, persona_mp


st.set_page_config(
    page_title=change_session_state(bundle)[0],
    page_icon=change_session_state(bundle)[3],
    layout="wide",
    initial_sidebar_state="expanded",
)
persona_name, persona_image, persona_description, persona_icon = bundle
image = process_image(persona_image)
persona_index, persona_map = get_maps()

# -----------------------------------------
# Unsupported, may break if the app changes.
# adjusts the style of side bar to keep the
# page options at the top
st.markdown(
    """
<style>
.css-1oe5cao {
    max-height: 10vh;
    list-style: none;
    overflow: overlay;
    margin: 0px;
    padding: 0px;
    padding-top: 0rem;
    padding-bottom: 0rem;
}
</style>
""",
    unsafe_allow_html=True,
)
# -----------------------------------------


def get_persona_names() -> Tuple[List[str], List[int]]:
    index_list = []
    name_list = []
    for index, persona_list_name in enumerate(json.loads(persona_index)):
        name_list.append(persona_list_name)
        index_list.append(index)
    return name_list, index_list


maps, indexes = get_persona_names()
persona_names = list(maps)
# logger.info(persona_index)
with st.sidebar:
    with st.container():
        st.markdown(persona_name)
        st.image(image)
        st.markdown(persona_description)

        selected_option = st.selectbox(
            label="Select Persona",
            key="persona_select",
            index=0,
            options=["Taimi", "Meg", "Max"],
            placeholder="Change Personas",
        )
        if selected_option := persona_name:
            change_session_state(
                (persona_name, persona_image, persona_description, persona_icon)
            )


def call_text_api(send_message: Message):
    logger.info("Calling API with message")
    api_url = f"{API_URL}text"
    payload = send_message.model_dump()
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Insomnia/2023.5.3",
    }
    request = requests.post(url=api_url, json=payload, headers=headers, timeout=60)
    logger.debug(request.status_code)
    return request


if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    # print(type(message))
    role = message.get("role")
    content = message.get("content")
    with st.chat_message(role):
        st.markdown(content)

if prompt := st.chat_input("prompt"):
    state_message = st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )
    with st.chat_message("user"):
        st.markdown(prompt)
    new_message = Message(role="user", content=prompt)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        response = call_text_api(send_message=new_message)
        if response.status_code != 200:
            st.error(f"Error: Please try again later: \n{response.status_code}")
            st.stop()
        res = json.loads(response.content.decode("utf-8"))
        res = json.loads(res)
        response = json.loads(res)
        logger.info(response)
        for message in response:
            full_response += response.get("content", "")
            message_placeholder.markdown(f"{full_response}▌")
        message_placeholder.markdown(full_response)
    if not isinstance(response, dict):
        response = {"role": "assistant", "content": str(response)}

    state_message = st.session_state.messages.append(response)
