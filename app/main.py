from fastapi import FastAPI
from app.routes import cadastro_cliente


app = FastAPI()

app.include_router(cadastro_cliente.router, tags=["Clientes"])