from pydantic import EmailStr, BaseModel
from sqlalchemy.orm import Session
from app.databases.models.cliente import Cliente
from app.databases.models.endereco_cliente import Endereco
from app.databases.models.telefone_cliente import TelefoneCliente, TipoTelefone
from app.databases.models.login import Login




# Tabela Cliente
class ClienteBase(BaseModel):
    nome_completo: str
    email: EmailStr
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


# Classe para combinar todos:
class ClienteCreate(BaseModel):
    cliente: ClienteBase
    telefone: TelefoneBase
    endereco: EnderecoBase