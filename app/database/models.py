from datetime import date
from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey, Table, Text
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

movie_actor_association = Table(
    'movie_actors',
    Base.metadata,
    Column('movie_id', Integer, ForeignKey('movies.id'), primary_key=True),
    Column('actor_id', Integer, ForeignKey('actors.id'), primary_key=True)
)


class Movie(Base):
    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(255), nullable=False)
    release_date = Column(Date, nullable=False)
    runtime = Column(Integer, nullable=False)
    synopsis = Column(Text, nullable=True)
    poster_url = Column(String(500), nullable=True)
    language = Column(String(100), nullable=False)
    genres = Column(String(500), nullable=True)
    budget = Column(Float, nullable=True)
    revenue = Column(Float, nullable=True)

    actors = relationship('Actor', secondary=movie_actor_association, back_populates='movies')
    ratings = relationship('Rating', back_populates='movie', cascade='all, delete-orphan')


class Actor(Base):
    __tablename__ = 'actors'

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    birth_date = Column(Date, nullable=True)
    nationality = Column(String(100), nullable=True)

    movies = relationship('Movie', secondary=movie_actor_association, back_populates='actors')


class Rating(Base):
    __tablename__ = 'ratings'

    id = Column(Integer, primary_key=True, autoincrement=True)
    score = Column(Float, nullable=False)
    review_text = Column(Text, nullable=True)
    reviewer_email = Column(String(255), nullable=True)
    movie_id = Column(Integer, ForeignKey('movies.id'), nullable=False)

    movie = relationship('Movie', back_populates='ratings')
