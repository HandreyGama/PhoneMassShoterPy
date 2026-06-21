"""
Arquivo responsavel por lidar com as requisiçoes para a API do Z-API
"""

import requests
import datetime
from src.models.consts import ZAPI_REQUESTS_SEND_TEXT,ZAPI_REQUESTS_CONTACTS,ZAPI_REQUESTS_TOKEN
from src.repositories.repositories import TelefoneRepository,TelefoneVistoRepository
from src.services.logs import *
headers = {
        "Client-Token": ZAPI_REQUESTS_TOKEN,
        "Content-Type": "application/json",
        }
def enviar_mensagem(phone_number:str,message:str):
    """
    Envia uma mensagem para o numero de telefone no formato DDI DDD Numero
    Dado numero e a mensagem
    """
    print(f"* enviando mensagem para:{phone_number}")
    data = {
        "phone": phone_number,
        "message": message
    }
    req = requests.post(url=ZAPI_REQUESTS_SEND_TEXT,headers=headers,json=data)
    

    if req.status_code == 200:
        status = "SUCESSO"
        print(f"* mensagem enviada com sucesso | StatusCode[{req.status_code}] ")
        info_message(f"A mensagem foi enviada com sucesso para: {phone_number} | StatusCode[{req.status_code}]")
    else:
        status = "FALHA"  
        print(f"[ERROR] falha no envido da mensagem | StatusCode[{req.status_code}]")
        error_message(f"erro no envio de mesagem | StatusCode[{req.status_code}]")
    return status
def enviar_mensagem_padrao():
    """
    Pega todos os numeros do banco de dados e envia a mensagem padrão para cada um
    """
    telefone_repo = TelefoneRepository()
    telefone_visto_repo = TelefoneVistoRepository()
    todos_contatos = telefone_repo.buscar_todos_telefones()
    for telefone in todos_contatos:
        print("==== Contato atual ====")
        print(f"| {telefone.nome_contato} - {telefone.telefone} |")
        status = enviar_mensagem(telefone.telefone,f"Olá, {telefone.nome_contato} tudo bem com você?")
        telefone_visto_repo.inserir_telefone_visto(telefone.telefone,telefone.id,status,datetime.datetime.now())
        print("==== FIM ====")
