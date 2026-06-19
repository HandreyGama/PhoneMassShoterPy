from src.database.db import base, engine
from src.models.consts import TELEFONE_REGEX_PATTERN
from sqlalchemy import Integer, Column, String, ForeignKey, Enum
from sqlalchemy.orm import validates, relationship
import enum
import re

class Telefone(base):
    __tablename__ = "telefones"

    id = Column(Integer,primary_key=True,index=True)
    telefone = Column(String,unique=True,nullable=False)
    nome_contato = Column(String,nullable=False)
    telefones_vistos_link = relationship('TelefoneVisto',back_populates='telefone_link')

    @validates('telefone')
    def validar_telefone(self,key,valor_telefone):
        if not re.match(TELEFONE_REGEX_PATTERN,valor_telefone):
            raise ValueError("Erro, endereço de telefone invalido!")
        else:
            return valor_telefone

    def __str__(self):
        return f"Telefone ID:{self.id}, TELEFONE NUMBER: {self.telefone}"
    
class StatusClass(enum.Enum):
    SUCESSO = 1,
    FALHA = 2,      
class TelefoneVisto(base):
    __tablename__ = "telefones_vistos"

    id = Column(Integer,primary_key=True,index=True)
    telefone = Column(String,unique=True,nullable=False)
    status = Column(Enum(StatusClass),unique=True,nullable=False)
    tid = Column(Integer,ForeignKey('telefones.id'))
    telefone_link = relationship('Telefone',back_populates='telefones_vistos_link')


base.metadata.create_all(bind=engine)