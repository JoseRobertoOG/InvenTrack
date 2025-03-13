from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker




# Endereço do banco de dados
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/postgres"


# Criação do engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Sessão local do banco de dados
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base do modelo
Base = declarative_base()

# Função para obter uma sessão do banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()