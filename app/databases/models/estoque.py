from sqlalchemy import Column, INTEGER, FLOAT, VARCHAR, ForeignKey
from app.databases.config import Base




class Estoque(Base):
    __tablename__ = "Estoque"

    idEstoque = Column(INTEGER, primary_key=True, nullable=False, unique=True, autoincrement=True)
    nome = Column(VARCHAR(40), nullable=False)
    capacidadeMaxima = Column(INTEGER, nullable=False)
    taxaSaida = Column(FLOAT, nullable=False)
    posicaoX = Column(INTEGER, nullable=False)
    poscaoY = Column(INTEGER, nullable=False)

    id_Simulacao = Column(INTEGER,
                          ForeignKey("Simulacao.idSimulacao",
                                     ondelete="CASCADE",
                                     onupdate="CASCADE",
                                     name="FK_Estoque_Simulacao"
                                     )
                          )