from sqlalchemy import Column, CHAR, VARCHAR, INTEGER, Enum, ForeignKey
from app.databases.config import Base
import enum



# Enum para o tipo de telefone:
class TipoTelefone(enum.Enum):
    COMERCIAL = "comercial"
    RESIDENCIAL = "residencial"
    PESSOAL = "pessoal"


class TelefoneCliente(Base):
    __tablename__ = "TelefoneCliente"
    idTelefoneCliente = Column(INTEGER, primary_key=True, unique=True, nullable=False, autoincrement=True)
    codPais = Column(VARCHAR(4), nullable=False)
    numero = Column(VARCHAR(20), nullable=False, unique=True)
    tipoTelefone = Column(Enum(TipoTelefone), nullable=False)

    # Foreign Key para a tabela Cliente
    id_cliente = Column(INTEGER,
                        ForeignKey("Cliente.idCliente",
                                   onupdate="CASCADE",
                                   ondelete="CASCADE",
                                   name="FK_cliente_telefone"
                                   )
                        )
