from src.models.models import Telefone, TelefoneVisto
from src.database.db import sessao_database
from sqlalchemy import select
class TelefoneRepository:
    def __init__(self) -> None:
        pass

    def inserir_telefone(self,telefone_number:str,nome_contato) -> Telefone:
        with sessao_database() as sessao:
            novo_telefone = Telefone(telefone=telefone_number,nome_contato=nome_contato)
            sessao.add(novo_telefone)
    def buscar_todos_telefones(self):
        with sessao_database() as sessao:
            stmt = select(Telefone)
            resultados = sessao.scalars(stmt).all()
            return resultados
    def buscar_telefone_por_numero(self,telefone_number:str):
        with sessao_database() as sessao:
            stmt = select(Telefone).where(Telefone.telefone == telefone_number)
            resultados = sessao.scalars(stmt).first()
            return resultados
    def buscar_nome_contato_por_telefone(self,telefone_number:str):
        with sessao_database() as sessao:
            stmt = select(Telefone).where(Telefone.telefone == telefone_number)
            telefone = sessao.scalars(stmt).first()
            return telefone.nome_contato         
class TelefoneVistoRepository:
    def __init__(self) -> None:
        pass
    def inserir_telefone_visto(self,telefone_number:str,tid,status) -> Telefone:
        with sessao_database() as sessao:
            novo_telefone = TelefoneVisto(telefone=telefone_number,tid=tid,status=status)
            sessao.add(novo_telefone)
    def buscar_todos_telefones_vistos(self):
        with sessao_database() as sessao:
            stmt = select(TelefoneVisto)
            resultados = sessao.scalars(stmt).all()
            return resultados
    def buscar_telefone_por_numero(self,telefone_number:str):
        with sessao_database() as sessao:
            stmt = select(TelefoneVisto).where(TelefoneVisto.telefone == telefone_number)
            resultados = sessao.scalars(stmt).first()
            return resultados                  