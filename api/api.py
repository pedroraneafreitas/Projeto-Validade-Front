import requests 

linkBase = "http://localhost:8080"

def getAllItens():
    return requests.get(linkBase + "/itens").json()
