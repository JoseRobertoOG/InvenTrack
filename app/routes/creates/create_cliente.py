from pydantic import BaseModel
from app.databases.models.telefone_cliente import TipoTelefone





# Tabela Cliente
class ClienteBase(BaseModel):
    nome_completo: str
    email: str
    cpf: str
    genero: str
    data_nascimento: str


# Tablea telefone
class TelefoneBase(BaseModel):
    telefone1: str
    tipo_telefone1: TipoTelefone
    telefone2: str | None = None
    tipo_telefone2: TipoTelefone | None = None
    telefone3: str | None = None
    tipo_telefone3: TipoTelefone | None = None


# Tabela Endereco
class EnderecoBase(BaseModel):
    cep: str
    pais: str
    estado: str
    cidade: str
    bairro: str
    rua: str  | None = None
    numero: str | None = None
    complemento: str | None = None


# Tabela Login
class LoginBase(BaseModel):
    username: str
    senha: str
    confirmacao_senha: str


# Classe para combinar todos:
class ClienteCreate(BaseModel):
    cliente: ClienteBase
    telefone: TelefoneBase
    endereco: EnderecoBase
    login: LoginBase