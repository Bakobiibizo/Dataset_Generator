from enum import Enum
from data_collectors import (
    run_PDF,
    run_HTML,
    run_XML,
    run_TXT,
    run_JSON,
    run_CSV,
    run_PY,
    run_URL,
)


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
