from sqlalchemy import Column, INTEGER, FLOAT, VARCHAR, ForeignKey
from app.databases.config import Base




class Maquina(Base):
    __tablename__ = "Maquina"

    idMaquina = Column(INTEGER, primary_key=True, unique=True, nullable=False, autoincrement=True)
    nome = Column(VARCHAR(40), nullable=False)
    estoqueEntrada = Column(INTEGER, nullable=False)
    estoqueSaida = Column(INTEGER, nullable=False)
    taxaEntrada = Column(FLOAT, nullable=False)
    taxaSaida = Column(FLOAT, nullable=False)
    posicaoX = Column(INTEGER, nullable=False)
    posicaoY = Column(INTEGER, nullable=False)

    id_Simulacao = Column(INTEGER,
                          ForeignKey("Simulacao.idSimulacao",
                                     ondelete="CASCADE",
                                     onupdate="CASCADE",
                                     name="FK_Maquina_Simulacao"
                                     )
                          )