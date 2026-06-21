import logging
from src.models.consts import ROOT_DIRECTORY
import datetime
logger = logging.getLogger(__name__)

logging.basicConfig(filename=(ROOT_DIRECTORY / "logs" / "logs.txt").as_posix(),level=logging.INFO)


def info_message(message):
    """
    Cria uma informação de log e coloca no arquivo log.txt na pasta logs
    """
    logger.info(str(datetime.datetime.now()) + message)

def warning_message(message):
    """
    Cria um aviso de log e coloca no arquivo log.txt na pasta logs
    """
    logger.warning(str(datetime.datetime.now()) + message)

def error_message(message):
    """
    Cria um aviso de erro no log e coloca no arquivo log.txt na pasta logs
    """
    logger.error(str(datetime.datetime.now()) + message)        
    print(f"Erro na execução do programa, veja em {ROOT_DIRECTORY / "logs" / "logs.txt"} para saber mais")