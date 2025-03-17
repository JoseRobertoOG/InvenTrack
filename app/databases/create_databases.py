from .config import engine
from .models.cliente import Cliente
from .models.endereco_cliente import Endereco
from .models.telefone_cliente import TelefoneCliente
from .models.login import Login
from .models.esteira import Esteira
from .models.maquina import Maquina
from .models.estoque import Estoque
from .models.movimentacao import Movimentacao
from .models.simulacao import Simulacao
from .models.produto import Produto



def create_databases():
    Cliente.__table__.create(bind=engine) # Criar tabela Cliente
    Endereco.__table__.create(bind=engine) # Criar tabela Endereco
    TelefoneCliente.__table__.create(bind=engine) # Criar tabela TelefoneCliente
    Login.__table__.create(bind=engine) # Criar tabela Login
    Esteira.__table__.create(bind=engine) # Criar tabela Esteira
    Maquina.__table__.create(bind=engine) # Criar tabela Maquina
    Estoque.__table__.create(bind=engine) # Criar tabela Estoque
    Movimentacao.__table__.create(bind=engine) # Criar tabela Movimetacao
    Simulacao.__table__.create(bind=engine) # Criar tabela Simulacao
    Produto.__table__.create(bind=engine) # Criar tabela Produto


create_databases()