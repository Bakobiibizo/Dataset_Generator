import requests
from local_files import save_local_file


def requestion_text_compression(data):
    compression_url = "http://localhost:8015/compression"
    result = requests.post(compression_url, data={"data": data}, timeout=120)
    compressed_transcripts = result.text
    file_name = save_local_file(compressed_transcripts)
    return compressed_transcripts, file_name
