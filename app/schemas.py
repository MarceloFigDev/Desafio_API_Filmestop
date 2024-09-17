from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class MovieBase(BaseModel):
    title: str
    genre: str

class MovieCreate(MovieBase):
    pass

class Movie(MovieBase):
    id: int
    rating_final: float
    total_ratings: int

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    name: str
    email: str

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int

    class Config:
        orm_mode = True

class Rental(BaseModel):
    user_id: int
    movie_id: int
    rental_date: datetime

    class Config:
        orm_mode = True

class Rating(BaseModel):
    user_id: int
    movie_id: int
    score: float

    class Config:
        orm_mode = True
