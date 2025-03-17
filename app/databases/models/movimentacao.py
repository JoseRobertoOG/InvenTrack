from sqlalchemy import Column, INTEGER, TIMESTAMP, Enum, ForeignKey, func
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



class Movimentacao(Base):
    __tablename__ = "Movimentacao"

    idMovimentacao = Column(INTEGER, primary_key=True, nullable=False, unique=True, autoincrement=True)
    tipoOrigem = Column(Enum(TipoOrigem), nullable=False)
    origemID = Column(INTEGER, nullable=False)
    tipoDestino = Column(Enum(TipoDestino), nullable=False)
    destinoId = Column(INTEGER, nullable=False)
    quantidade = Column(INTEGER, nullable=False)
    dataMovimentacao = Column(TIMESTAMP, nullable=False, server_default=func.now())

    id_Simulacao = Column(INTEGER,
                          ForeignKey("Simulacao.idSimulacao",
                                     ondelete="CASCADE",
                                     onupdate="CASCADE",
                                     name="FK_Movimentacao_Simulacao"
                                     )
                          )
    
    id_Produto = Column(INTEGER,
                        ForeignKey("Produto.idProduto",
                                   ondelete="CASCADE",
                                   onupdate="CASCADE",
                                   name="FK_Movimentacao_Produto"
                                   )
                        )