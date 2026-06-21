from time import sleep
from random import randrange

from src.services.api import enviar_mensagem_padrao

class ApiService:
    def __init__(self) -> None:
        pass
    def enviar_mensagem(self,rate_limit:int=0):
        if type(rate_limit) is not int:
            raise ValueError("ERRO, tipo do rate_limit tem que ser Inteiro")
        elif rate_limit < 0:
            raise ValueError("ERRO, valor do rate_limite não pode ser menor que 0")
        if rate_limit == 0:
            enviar_mensagem_padrao()
        else:
            sleep(rate_limit + randrange(0,7))
            enviar_mensagem_padrao()


