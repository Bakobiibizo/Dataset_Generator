import json
import loguru
import requests
from data_models import Message

logger = loguru.logger

API_URL = "http://localhost:8555/"


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


def request_chat(new_message: Message):
    response = call_text_api(send_message=new_message)
    if response.status_code != 200:
        logger.error(f"Error: Please try again later: \n{response.status_code}")
    res = json.loads(response.content.decode("utf-8"))
    res = json.loads(res)
    response = json.loads(res)
    logger.info(response)
