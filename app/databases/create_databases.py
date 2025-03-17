from app.databases.config import engine
from app.databases.models.cliente import Cliente
from app.databases.models.endereco_cliente import Endereco
from app.databases.models.telefone_cliente import TelefoneCliente
from app.databases.models.login import Login
from app.databases.models.esteira import Esteira
from app.databases.models.maquina import Maquina
from app.databases.models.estoque import Estoque
from app.databases.models.movimentacao import Movimentacao
from app.databases.models.simulacao import Simulacao
from app.databases.models.produto import Produto


def create_databases():
    """ 
    Criacao das tabelas no db postgres
    Lembre-se de alterar o caminho do db em app > databases > config.py
    Retirar as # das tabelas que deseja criar
    Comando Bash para criar as DT: python -m app.databases.create_databases
    """

    #Cliente.__table__.create(bind=engine) # Criar tabela Cliente
    #Endereco.__table__.create(bind=engine) # Criar tabela Endereco
    #TelefoneCliente.__table__.create(bind=engine) # Criar tabela TelefoneCliente
    #Login.__table__.create(bind=engine) # Criar tabela Login
    #Simulacao.__table__.create(bind=engine) # Criar tabela Simulacao
    #Produto.__table__.create(bind=engine) # Criar tabela Produto
    #Esteira.__table__.create(bind=engine) # Criar tabela Esteira
    #Maquina.__table__.create(bind=engine) # Criar tabela Maquina
    #Estoque.__table__.create(bind=engine) # Criar tabela Estoque
    #Movimentacao.__table__.create(bind=engine) # Criar tabela Movimetacao


# create_databases()