from sqlalchemy import Column, FLOAT, INTEGER, ForeignKey, Enum
from app.databases.config import Base
import enum



# criacao do enum para tipo de origem
class TipoOrigem(enum.Enum):
    ESTOQUE = "estoque"
    MAQUINA = "maquina"

# criacao do enum para tipo de destino
class TipoDestino(enum.Enum):
    ESTOQUE = "estoque"
    MAQUINA = "maquina"


class Esteira(Base):
    __tablename__ = "Esteira"

    idEsteira = Column(INTEGER, primary_key=True, unique=True, nullable=False, autoincrement=True)
    velocidade = Column(FLOAT, nullable=False)
    origemTipo = Column(Enum(TipoOrigem), nullable=False)
    origemId = Column(INTEGER, nullable=False)
    destinoTipo = Column(Enum(TipoDestino), nullable=False)
    destinoId = Column(INTEGER, nullable=False)

    id_Simulacao = Column(INTEGER, ForeignKey("Simulacao.idSimulacao",
                                              ondelete="CASCADE",
                                              onupdate="CASCADE",
                                              name="FK_Esteira_Simulacao"
                                              )
                          )
    