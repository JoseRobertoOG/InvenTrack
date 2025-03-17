from sqlalchemy import Column, INTEGER, VARCHAR, ForeignKey, BOOLEAN, TIMESTAMP, DATETIME, func
from app.databases.config import Base




class Login(Base):
    __tablename__ = "Login"

    idLogin = Column(INTEGER, primary_key=True, unique=True, nullable=False, autoincrement=True)
    username = Column(VARCHAR(20), unique=True, nullable=False,)
    senhaHASH = Column(VARCHAR(255), unique=True, nullable=False)
    email = Column(VARCHAR(100), unique=True, nullable=False)
    dataRegistro = Column(TIMESTAMP, nullable=False, server_default=func.now())
    ultimoLogin = Column(DATETIME, nullable=True)
    estaAtivo = Column(BOOLEAN, nullable=False)

    id_Cliente = Column(INTEGER,
                        ForeignKey("Cliente.idCliente",
                                    ondelete="CASCADE",
                                    onupdate="CASCADE",
                                    name="FK_Login_Cliente"
                                    )
                        )

