from src.models.consts import DATABASE_URL

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.pool import NullPool
from contextlib import contextmanager
engine = create_engine(DATABASE_URL,poolclass=NullPool,echo=True)
session = sessionmaker(autocommit=False,autoflush=False,bind=engine,expire_on_commit=False,)
base = declarative_base()

@contextmanager
def sessao_database():
    sessao = session()
    try:
        yield sessao
        sessao.commit()
    except Exception:
        sessao.rollback()
        raise    
    finally:
        sessao.close()    