import os
import requests
from requests.exceptions import HTTPError
from local_files import save_local_file


def call_scraper(url):
    response = None
    response = requests.post(url, json={"url": url}, timeout=30)
    filename = save_local_file(response.text)
    return response.text, filename


if __name__ == "__main__":
    url = input("Target URL: ")
    print(call_scraper(url=url))
