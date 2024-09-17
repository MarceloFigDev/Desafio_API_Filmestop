from sqlalchemy.orm import Session
from app import models, schemas

def get_movies_by_genre(db: Session, genre: str):
    return db.query(models.Movie).filter(models.Movie.genre == genre).all()

def get_movie(db: Session, movie_id: int):
    return db.query(models.Movie).filter(models.Movie.id == movie_id).first()

def create_rental(db: Session, rental: schemas.Rental):
    db_rental = models.Rental(**rental.dict())
    db.add(db_rental)
    db.commit()
    db.refresh(db_rental)
    return db_rental

def rate_movie(db: Session, movie_id: int, user_id: int, score: float):
    rating = models.Rating(movie_id=movie_id, user_id=user_id, score=score)
    db.add(rating)
    
    movie = db.query(models.Movie).filter(models.Movie.id == movie_id).first()
    movie.total_ratings += 1
    movie.rating_final = (movie.rating_final * (movie.total_ratings - 1) + score) / movie.total_ratings
    
    db.commit()
    return rating