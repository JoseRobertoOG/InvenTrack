from sqlalchemy import Column, VARCHAR, INTEGER, ForeignKey
from app.databases.config import Base




class Produto(Base):
    __tablename__ = "Produto"

    idProduto = Column(INTEGER, primary_key=True, unique=True, nullable=False, autoincrement=True)
    nome = Column(VARCHAR(40), nullable=False)
    formato = Column(VARCHAR(20), nullable=False)
    cor = Column(VARCHAR(20), nullable=False)

    id_Simulacao = Column(INTEGER, ForeignKey("Simulacao.idSimulacao",
                                              ondelete="CASCADE",
                                              onupdate="CASCADE",
                                              name="FK_Produto_Simulacao"
                                              )
                          )
    
