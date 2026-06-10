import requests
from pathlib import Path

URL = "https://localhost:8000/request_ollama/"
CERT_PATH = r"C:\Users\thomas\Documents\Projet_stage_backend\src\library\certs\api-cert.pem"

def ask_api(m: str):
    payload = {
        "question": m,
    }

    response = requests.post(
        URL,
        json=payload,
        verify=CERT_PATH,
        timeout=60
    )
    response.raise_for_status()
    return response