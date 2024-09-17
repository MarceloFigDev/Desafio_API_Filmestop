from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app import crud, schemas
from app.database import get_db

router = APIRouter()

@router.post("/users", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    """
    Endpoint para criar um novo usuário.
    """
    return crud.create_user(db, user)

@router.get("/users", response_model=List[schemas.User])
def list_users(db: Session = Depends(get_db)):
    """
    Endpoint para listar todos os usuários.
    """
    return crud.get_users(db)

@router.get("/users/{user_id}", response_model=schemas.User)
def get_user(user_id: int, db: Session = Depends(get_db)):
    """
    Endpoint para obter detalhes de um usuário específico pelo ID.
    """
    return crud.get_user(db, user_id)
