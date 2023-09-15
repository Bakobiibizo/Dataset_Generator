import os
import json
import streamlit as st
from data_models import Data, data_map


st.title("Data Collection")

download_file_path = ""

with st.sidebar:
    sidebar_container = st.container()
url = sidebar_container.text_input("Enter target URL:")
local_file = sidebar_container.file_uploader("or Upload your data")


options = [
    Data.PDF.value,
    Data.HTML.value,
    Data.XML.value,
    Data.TXT.value,
    Data.JSON.value,
    Data.CSV.value,
    Data.PY.value,
    Data.URL.value,
]

data_type = sidebar_container.selectbox(
    label="Data Type",
    options=options,
    key="Data Type",
    placeholder=options[0],
    index=0,
)
main_container = st.container()
main_container.write()
download_path = st.text_area
if not data_type:
    data_type = options[0]
if sidebar_container.button("Submit"):
    file_path = ""
    for i, _ in enumerate(os.listdir("tmp")):
        print(i)
        print(_)
        file_path = f"tmp/temp_file{i}{data_type.lower()}"
        print(file_path)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(json.dumps(local_file))

    collection_function = data_map[data_type]
    data = collection_function(file_path, url)
    main_container.write(data)
    download_file_path = file_path
    download_path.write(file_path)
    print(data)

st.sidebar.download_button(
    label="Download File",
    file_name=download_file_path,
    data=json.dumps(download_file_path),
)


def get_download_path():
    return download_path
