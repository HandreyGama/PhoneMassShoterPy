"""
Arquivo contendo todas as constantes do programa
Como: 
- Variaveis de ambiente
- Caminho de arquivos
- Padrões de REGEX
- Entre outros
"""


from pathlib import Path
from dotenv import load_dotenv
import os
load_dotenv()

DATABASE_USER = os.getenv("user")
DATABASE_PASSWORD = os.getenv("password")
DATABASE_HOST = os.getenv("host")
DATABASE_PORT = os.getenv("port")
DATABASE_DBNAME = os.getenv("dbname")
ROOT_DIRECTORY = Path(__file__).absolute().resolve().parents[2]
DATABASE_URL = f"postgresql+psycopg2://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_DBNAME}?sslmode=require"
ZAPI_REQUESTS_URL = os.getenv('zapi_instance')
ZAPI_REQUESTS_SEND_TEXT = ZAPI_REQUESTS_URL + "send-text"
ZAPI_REQUESTS_CONTACTS = ZAPI_REQUESTS_URL + "contacts"
ZAPI_REQUESTS_TOKEN = os.getenv('zapi_instance')
TELEFONE_REGEX_PATTERN = r"^\+55\d{11}"