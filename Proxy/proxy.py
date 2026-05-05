import requests
import json

URL = "http://127.0.0.1:8000/"


def get_historique():
    url = URL +"taches/"
    response = requests.get(url)
    response.raise_for_status() 
    data = response.json()
    return data      

def  post_question(message : str):
    url = URL + "request_ollama/"
    payload = {
        "question" : message,
    }

    reponse = requests.post(url, json=payload)
    return reponse




