from sqlalchemy import Column, Integer, DateTime, VARCHAR, CHAR, Enum, DATE
from app.databases.config import Base
import enum



# Enum para o genero do cliente
class Genero(enum.Enum):
    MASCULINO = "m"
    FEMININO = "f"
    OUTRO = "o"

# Modelagem da Tabela Cliente:

class Cliente(Base):
    __tablename__ = "Cliente"


    idCliente = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    nomeCompleto = Column(VARCHAR(100), nullable=False)
    email = Column(VARCHAR(100), nullable=False, unique=True)
    cpf = Column(CHAR(11), nullable=False, unique=True) # CPF armazenado no formato XXXXXXXXXXX
    genero = Column(Enum(Genero), nullable=False)
    dataNascimento = Column(DATE, nullable=False)
    dataRegistro = Column(DateTime, nullable=False)