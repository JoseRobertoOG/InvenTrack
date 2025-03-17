from sqlalchemy import Column, INTEGER, CHAR, VARCHAR, ForeignKey
from app.databases.config import Base




class Endereco(Base):
    __tablename__ = "Endereco"

    idEndereco = Column(INTEGER, primary_key=True, unique=True, nullable=False, autoincrement=True)
    cep = Column(VARCHAR(20), nullable=False)
    pais = Column(VARCHAR(40), nullable=False)
    estado = Column(CHAR(2), nullable=False) # No formato XX
    cidade = Column(VARCHAR(40), nullable=False)
    bairro = Column(VARCHAR(40), nullable=False)
    rua = Column(VARCHAR(40), nullable=True)
    numero = Column(VARCHAR(6), nullable=False)
    complemento = Column(VARCHAR(100), nullable=False)

    id_Cliente = Column(INTEGER,
                        ForeignKey("Cliente.idCliente",
                                   ondelete="CASCADE",
                                   onupdate="CASCADE",
                                   name="FK_Endereco_Cliente"
                                   )
                        )