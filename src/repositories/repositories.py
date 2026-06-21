"""
Arquivo responsavel por Fazer a manipulação de dados no database

"""


from src.models.models import Telefone, TelefoneVisto
from src.database.db import sessao_database
from sqlalchemy import select
from src.services.logs import *
import datetime


class TelefoneRepository:
    def __init__(self) -> None:
        pass

    def inserir_telefone(self,telefone_number:str,nome_contato) -> Telefone:
        """
        Insere um numero de telefone na tabela Telefones 
        Do banco de dados. dado numero de telefone no padrão [DDI DDD Numero]
        e o nome do contato.
        """
        try:
            with sessao_database() as sessao:
                novo_telefone = Telefone(telefone=telefone_number,nome_contato=nome_contato)
                sessao.add(novo_telefone)
                info_message(f"Numero de telefone {telefone_number} cadastrado com sucesso!")
        except Exception as e:
            error_message(f"Erro ao tentar inserir numero de telefone: {telefone_number}\n{e}")

    def buscar_todos_telefones(self):
        """
        Retorna todos os telefones cadastrados na tabela Telefones Do banco de dados.
        """
        try:
            with sessao_database() as sessao:
                stmt = select(Telefone)
                resultados = sessao.scalars(stmt).all()
                return resultados
            warning_message("Nenhum usuario encontrado no banco de dados")
        except Exception as e:
            error_message(f"Erro ao tentar buscar todos os telefone\n{e}")
        return None 
    def buscar_telefone_por_numero(self,telefone_number:str) -> Telefone | None:
        """
        Retorna um numero de telefone na tabela Telefones no banco de dados.
        dado numero de telefone no padrão [DDI DDD Numero]
        """
        try:
            with sessao_database() as sessao:
                stmt = select(Telefone).where(Telefone.telefone == telefone_number)
                resultados = sessao.scalars(stmt).first()
                return resultados
            error_message(f"Erro, numero {telefone_number} não encontrado no banco de dados")
        except Exception as e:
            error_message(f"Erro ao tentar buscar numero de telefone: {telefone_number}\n{e}")                
        return None

class TelefoneVistoRepository:
    def __init__(self) -> None:
        pass
    def inserir_telefone_visto(self,telefone_number:str,tid,status,data:datetime.datetime) -> None:
        """
        Insere um numero de telefoneVisto na tabela telefones_vistos no banco de dados.
        dado numero de telefone no padrão [DDI DDD Numero]
        o id correspondente do telefone na tabela telefones 
        e o status do envio(SUCESSO,FALHA)
        """
        try:
            with sessao_database() as sessao:
                novo_telefone = TelefoneVisto(telefone=telefone_number,tid=tid,status=status,data=data)
                sessao.add(novo_telefone)
                info_message(f"numero de telefone:{telefone_number} cadastrado com sucesso!")   
        except Exception as e:
            error_message(f"Erro ao tentar adicionar numero de telefone:{telefone_number} no banco de dados\n{e}")         
    def buscar_todos_telefones_vistos(self):
        """
        Retorna todos os numero de telefoneVisto no banco de dados 
        """
        try:
            with sessao_database() as sessao:
                stmt = select(TelefoneVisto)
                resultados = sessao.scalars(stmt).all()
                return resultados
        except Exception as e:
            error_message(f"Erro ao tentar buscar todos os numeros de telefone no banco de dados\n{e}")         
        return None
    def buscar_telefone_por_numero(self,telefone_number:str) -> TelefoneVisto | None:
        """
        Retorna um numero de telefoneVisto cadastrado no banco de dados 
        dado um numero de telefone no padrão [DDI DDD Numero]
        """
        try:
            with sessao_database() as sessao:
                stmt = select(TelefoneVisto).where(TelefoneVisto.telefone == telefone_number)
                resultados = sessao.scalars(stmt).first()
                return resultados  
        except Exception as e:
            error_message(f"Erro ao tentar buscar numero de telefone:{telefone_number} no banco de dados\n{e}")                   
        return None           