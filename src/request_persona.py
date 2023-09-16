import json
import loguru
import requests
from data_models import PersonaRequest
from typing import Tuple

API_URL = "http://localhost:8555/"

logger = loguru.logger


def call_persona_request(request: PersonaRequest):
    # logger.info(f"Calling API with new persona: {request}")
    api_url = f"{API_URL}persona"
    payload = request.model_dump()
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Insomnia/2023.5.3",
    }
    # logger.debug(f"Payload: {payload} \n Headers: {headers} \n URL: {api_url}")
    req = requests.post(api_url, json=payload, headers=headers, timeout=40)
    logger.debug(req.status_code)
    return req.content


def public_request(path: str):
    path = f"{API_URL}public/{path}"
    # logger.debug(path)
    request_response = requests.get(path, timeout=10)
    return request_response.content


def parse_persona_response(data):
    data = data.decode("utf-8")
    response = json.loads(data)
    dict_response = json.loads(response)
    persona_name = dict_response.get("name")
    persona_image = dict_response.get("image")
    persona_description = dict_response.get("description")
    pesona_icon = dict_response.get("icon")
    return persona_name, persona_image, persona_description, pesona_icon


def get_persona(persona_input: str = "persona"):
    persona_request = PersonaRequest(request_type=persona_input, content="persona")
    response = call_persona_request(persona_request)
    return parse_persona_response(response)


def get_persona_image(persona_image: str):
    return public_request(persona_image)


def get_persona_index():
    return public_request("persona_index.json")


def get_persona_map():
    return public_request("persona_map.json")
