import base64


def request_image():
    with open("src/public/1.png", "rb") as file:
        return base64.b64encode(file.read()).decode("utf-8")
