from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app import crud, schemas
from app.database import get_db

router = APIRouter()

@router.post("/rentals", response_model=schemas.Rental)
def create_rental(rental: schemas.Rental, db: Session = Depends(get_db)):
    """
    Endpoint para criar um aluguel de filme.
    """
    return crud.create_rental(db, rental)

@router.get("/rentals", response_model=List[schemas.Rental])
def list_rentals(db: Session = Depends(get_db)):
    """
    Endpoint para listar todos os aluguéis de filmes.
    """
    # Esta função pode ser expandida para adicionar filtros, como por usuário ou data.
    pass
