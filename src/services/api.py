import requests

from src.models.consts import ZAPI_REQUESTS_SEND_TEXT,ZAPI_REQUESTS_CONTACTS,ZAPI_REQUESTS_TOKEN
from src.repositories.repositories import TelefoneRepository,TelefoneVistoRepository
headers = {
        "Client-Token": ZAPI_REQUESTS_TOKEN,
        "Content-Type": "application/json",
        }
def enviar_mensagem(phone_number,message):
    data = {
        "phone": phone_number,
        "message": message
    }
    req = requests.post(url=ZAPI_REQUESTS_SEND_TEXT,headers=headers,json=data)
    print(req.status_code)  
    print(req.json())
    return req.status_code
def enviar_mensagem_padrao():
    telefone_repo = TelefoneRepository()
    telefone_visto_repo = TelefoneVistoRepository()
    todos_contatos = telefone_repo.buscar_todos_telefones()
    for telefone in todos_contatos:
        status_code = enviar_mensagem(telefone.telefone,f"Olá, {telefone.nome_contato} tudo bem com você?")
        if status_code == 200:
            status = "SUCESSO"
        else:
            status = "FALHA"    
        telefone_visto_repo.inserir_telefone_visto(telefone.telefone,telefone.id,status)
enviar_mensagem_padrao()