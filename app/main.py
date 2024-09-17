from fastapi import FastAPI
from app.routers import movies, rentals, users
from app.database import Base, engine

# Criação automática das tabelas no banco de dados
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Incluindo as rotas da API
app.include_router(movies.router)
app.include_router(rentals.router)
app.include_router(users.router)
