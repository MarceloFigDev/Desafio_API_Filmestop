from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app import crud, schemas
from app.database import get_db

router = APIRouter()

@router.get("/movies", response_model=List[schemas.Movie])
def list_movies_by_genre(genre: str, db: Session = Depends(get_db)):
    """
    Endpoint para listar filmes por gênero.
    """
    return crud.get_movies_by_genre(db, genre)

@router.get("/movies/{movie_id}", response_model=schemas.Movie)
def get_movie(movie_id: int, db: Session = Depends(get_db)):
    """
    Endpoint para obter os detalhes de um filme específico pelo ID.
    """
    return crud.get_movie(db, movie_id)
