import os
import json
import streamlit as st
from data_models import Data, data_map


st.title("Data Collection")

main_container = st.container()

st.header("Select a target Location local or url")
local_file = main_container.file_uploader("Upload your data")
url = main_container.text_input("Enter target location:")

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

data_type = main_container.selectbox(
    label="Data Type",
    options=options,
    key="Data Type",
    placeholder=options[0],
    index=0,
)
if not data_type:
    data_type = options[0]
if main_container.button("Submit"):
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
    print(data)
