from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.databases.config import get_db
from app.routes.creates.create_cliente import ClienteCreate





router = APIRouter()
@router.post("/singup/")

def cadastrar_cliente(
    dados: ClienteCreate,
    db: Session = Depends(get_db)
    ):

    pass