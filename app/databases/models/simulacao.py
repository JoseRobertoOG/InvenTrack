from sqlalchemy import Column, INTEGER, VARCHAR, ForeignKey, TIMESTAMP, func
from app.databases.config import Base




class Simulacao(Base):
    __tablename__ = "Simulacao"

    idSimulacao = Column(INTEGER, primary_key=True, unique=True, nullable=False, autoincrement=True)
    dataRegistro = Column(TIMESTAMP, nullable=False, server_default=func.now())
    nomeSimulacao = Column(VARCHAR(50), nullable=False, unique=True)

    id_Cliente = Column(INTEGER,
                        ForeignKey("Cliente.idCliente",
                                   ondelete="CASCADE",
                                   onupdate="CASCADE",
                                   name="FK_Simulacao_Cliente"
                                   )
                        )