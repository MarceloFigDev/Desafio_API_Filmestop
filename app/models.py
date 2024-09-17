from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime
from sqlalchemy.orm import relationship
from app.database import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    rentals = relationship("Rental", back_populates="user")

class Movie(Base):
    __tablename__ = 'movies'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    genre = Column(String, index=True)
    rating_final = Column(Float, default=0.0)
    total_ratings = Column(Integer, default=0)
    rentals = relationship("Rental", back_populates="movie")
    ratings = relationship("Rating", back_populates="movie")

class Rental(Base):
    __tablename__ = 'rentals'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    movie_id = Column(Integer, ForeignKey('movies.id'))
    rental_date = Column(DateTime)
    user = relationship("User", back_populates="rentals")
    movie = relationship("Movie", back_populates="rentals")

class Rating(Base):
    __tablename__ = 'ratings'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    movie_id = Column(Integer, ForeignKey('movies.id'))
    score = Column(Float)
    user = relationship("User")
    movie = relationship("Movie", back_populates="ratings")
