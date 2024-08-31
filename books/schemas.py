from pydantic import BaseModel, Field, field_validator, validator, ValidationError
from datetime import date, datetime
from sqlalchemy.orm import Session

from database import SessionLocal
from books import crud


class GenreBase(BaseModel):
    name: str = Field(min_length=2, max_length=50)


class GenreCreate(GenreBase):
    pass


class GenreUpdate(GenreBase):
    id: int


class Genre(GenreBase):
    id: int

    class Config:
        orm_mode = True


class AuthorBase(BaseModel):
    name: str = Field(min_length=2, max_length=100)
    surname: str = Field(min_length=2, max_length=100)
    date_of_birth: date
    country: str = Field(min_length=2, max_length=50)

    @classmethod
    @field_validator('date_of_birth')
    def validate_date_of_birth(cls, value):
        if value > date.today():
            raise ValueError('Date of birth cannot be in the future.')
        return value


class AuthorCreate(AuthorBase):
    pass


class AuthorUpdate(AuthorBase):
    id: int


class Author(AuthorBase):
    id: int

    class Config:
        orm_mode = True


class BookBase(BaseModel):
    title: str = Field(min_length=2, max_length=100)
    publication_date: date
    rating: int = Field(ge=1, le=10)
    description: str = Field(max_length=1000)

    @classmethod
    @field_validator('publication_date')
    def validate_publication_date(cls, value):
        if value > date.today():
            raise ValueError('Publication date cannot be in the future.')
        return value


class BookCreate(BookBase):
    author_id: int
    genre_id: int

    @classmethod
    @field_validator('author_id')
    def validate_author_exists(cls, value):
        db: Session = SessionLocal()
        author = crud.get_author(db, author_id=value)
        if author is None:
            raise ValueError(f'Author with id {value} does not exist.')
        return value

    @classmethod
    @field_validator('genre_id')
    def validate_genre_exists(cls, value):
        db: Session = SessionLocal()
        genre = crud.get_genre(db, genre_id=value)
        if genre is None:
            raise ValueError(f'Genre with id {value} does not exist.')
        return value


class BookUpdate(BookCreate):
    id: int


class Book(BookBase):
    id: int
    genre: Genre
    author: Author
    created_at: datetime

    class Config:
        orm_mode = True
