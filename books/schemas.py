from pydantic import BaseModel, Field, model_validator
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
        from_attributes = True


class AuthorBase(BaseModel):
    name: str = Field(min_length=2, max_length=100)
    surname: str = Field(min_length=2, max_length=100)
    date_of_birth: date
    country: str = Field(min_length=2, max_length=50)


class AuthorCreate(AuthorBase):

    @model_validator(mode='after')
    def check_passwords_match(self):
        if self.date_of_birth > date.today():
            raise ValueError('Date of birth cannot be in the future.')
        return self


class AuthorUpdate(AuthorBase):
    id: int


class Author(AuthorBase):
    id: int

    class Config:
        from_attributes = True


class BookBase(BaseModel):
    title: str = Field(min_length=2, max_length=100)
    publication_date: date
    rating: int = Field(ge=1, le=10)
    description: str = Field(max_length=1000)


class BookCreate(BookBase):
    author_id: int
    genre_id: int

    @model_validator(mode='after')
    def check_passwords_match(self):
        db: Session = SessionLocal()
        author = crud.get_author(db, author_id=self.author_id)
        if author is None:
            raise ValueError(f'Author with id {self.author_id} does not exist.')
        genre = crud.get_genre(db, genre_id=self.genre_id)
        if genre is None:
            raise ValueError(f'Genre with id {self.genre_id} does not exist.')
        if self.publication_date > date.today():
            raise ValueError('Publication date cannot be in the future.')
        return self


class BookUpdate(BookCreate):
    id: int


class Book(BookBase):
    id: int
    genre: Genre
    author: Author
    created_at: datetime

    class Config:
        from_attributes = True
