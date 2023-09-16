from typing import Optional
from request_collection import call_scraper
from request_compression import requestion_text_compression


def run_PDF(local_file: Optional[str] = None, url: Optional[str] = None):
    if not url:
        url = None
    return f"local_file: {local_file}"


def run_HTML(local_file: Optional[str] = None, url: Optional[str] = None):
    if not url:
        url = None
    return f"local_file: {local_file}"


def run_XML(local_file: Optional[str] = None, url: Optional[str] = None):
    if not url:
        url = None
    return f"local_file: {local_file}"


def run_TXT(local_file: Optional[str] = None, url: Optional[str] = None):
    if not url:
        url = None
    return f"local_file: {local_file}"


def run_JSON(local_file: Optional[str] = None, url: Optional[str] = None):
    if not url:
        url = None
    return f"local_file: {local_file}"


def run_CSV(local_file: Optional[str] = None, url: Optional[str] = None):
    if not url:
        url = None
    return f"local_file: {local_file}"


def run_PY(local_file: Optional[str] = None, url: Optional[str] = None):
    if not url:
        url = None
    return f"local_file: {local_file}"


def run_URL(local_file: Optional[str] = None, url: Optional[str] = None):
    if not local_file:
        local_file = None
    raw_data = call_scraper(url)
    return raw_data


def run_compression(data):
    compressed_data = requestion_text_compression(data)
    return compressed_data
