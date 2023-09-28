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
    return call_scraper(url)


def run_compression(data):
    return requestion_text_compression(data)
