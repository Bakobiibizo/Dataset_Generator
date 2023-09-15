from typing import Optional
from collection_request import call_scraper


def run_PDF(local_file: Optional[str] = None, url: Optional[str] = None):
    return f"local_file: {local_file}"


def run_HTML(local_file: Optional[str] = None, url: Optional[str] = None):
    return f"local_file: {local_file}"


def run_XML(local_file: Optional[str] = None, url: Optional[str] = None):
    return f"local_file: {local_file}"


def run_TXT(local_file: Optional[str] = None, url: Optional[str] = None):
    return f"local_file: {local_file}"


def run_JSON(local_file: Optional[str] = None, url: Optional[str] = None):
    return f"local_file: {local_file}"


def run_CSV(local_file: Optional[str] = None, url: Optional[str] = None):
    return f"local_file: {local_file}"


def run_PY(local_file: Optional[str] = None, url: Optional[str] = None):
    return f"local_file: {local_file}"


def run_URL(local_file: Optional[str] = None, url: Optional[str] = None):
    if not local_file:
        local_file = None
    result = call_scraper(url)
    return result
