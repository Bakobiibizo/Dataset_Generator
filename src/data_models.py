import loguru
import pydantic
from pydantic import BaseModel
from typing import Optional
from enum import Enum
from request_hub import (
    run_PDF,
    run_HTML,
    run_XML,
    run_TXT,
    run_JSON,
    run_CSV,
    run_PY,
    run_URL,
)


logger = loguru.logger


class Message(BaseModel):
    role: str
    content: str


class Prompt(Message):
    pass


class TextData(pydantic.BaseModel):
    text: str
    voice_id: Optional[str]

    @pydantic.validator("text")
    @classmethod
    def text_valid(cls, text):
        if text == "":
            raise ValueError("Text cannot be empty")
        else:
            return text


class PersonaRequest(BaseModel):
    request_type: str
    content: str

    @pydantic.validator("content")
    @classmethod
    def content_valid(cls, content):
        if content == "":
            raise ValueError("Content cannot be empty")
        else:
            return content

    @pydantic.validator("request_type")
    @classmethod
    def request_type_valid(cls, request_type):
        if request_type == "":
            request_type = "persona"
        else:
            return request_type


class Data(Enum):
    PDF = "PDF"
    HTML = "HTML"
    XML = "XML"
    TXT = "TXT"
    JSON = "JSON"
    CSV = "CSV"
    PY = "PY"
    URL = "URL"


data_map = {
    Data.PDF.value: run_PDF,
    Data.HTML.value: run_HTML,
    Data.XML.value: run_XML,
    Data.TXT.value: run_TXT,
    Data.JSON.value: run_JSON,
    Data.CSV.value: run_CSV,
    Data.PY.value: run_PY,
    Data.URL.value: run_URL,
}
