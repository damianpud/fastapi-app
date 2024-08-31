from sqlalchemy.orm import Session, joinedload
from sqlalchemy import select
from fastapi_pagination.ext.sqlalchemy import paginate

from books import models
from books import schemas


def get_genre(db: Session, genre_id: int):
    return db.query(models.Genre).filter(models.Genre.id == genre_id).first()


def get_genres(db: Session):
    return paginate(db, select(models.Genre))


def create_genre(db: Session, genre: schemas.GenreCreate):
    db_genre = models.Genre(
        name=genre.name
    )
    db.add(db_genre)
    db.commit()
    db.refresh(db_genre)
    return db_genre


def update_genre(db: Session, genre_id: int, genre_update: schemas.GenreUpdate):
    db_genre = get_genre(db, genre_id)
    if db_genre:
        update_data = genre_update.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_genre, key, value)
        db.commit()
        db.refresh(db_genre)
    return db_genre


def delete_genre(db: Session, genre_id: int):
    db_genre = get_genre(db, genre_id)
    if db_genre:
        db.delete(db_genre)
        db.commit()
    return db_genre


def get_author(db: Session, author_id: int):
    return db.query(models.Author).filter(models.Author.id == author_id).first()


def get_authors(db: Session):
    return paginate(db, select(models.Author))


def create_author(db: Session, author: schemas.AuthorCreate):
    db_author = models.Author(
        name=author.name,
        surname=author.surname,
        date_of_birth=author.date_of_birth,
        country=author.country,
    )
    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    return db_author


def update_author(db: Session, author_id: int, author_update: schemas.AuthorUpdate):
    db_author = get_author(db, author_id)
    if db_author:
        update_data = author_update.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_author, key, value)
        db.commit()
        db.refresh(db_author)
    return db_author


def delete_author(db: Session, author_id: int):
    db_author = get_author(db, author_id)
    if db_author:
        db.delete(db_author)
        db.commit()
    return db_author


def get_book(db: Session, book_id: int):
    return db.query(models.Book)\
        .options(joinedload(models.Book.author))\
        .options(joinedload(models.Book.author))\
        .filter(models.Book.id == book_id).first()


def get_books(db: Session):
    return paginate(db, select(models.Book))


def create_book(db: Session, book: schemas.BookCreate):
    db_book = models.Book(
        title=book.title,
        publication_date=book.publication_date,
        rating=book.rating,
        description=book.description,
        genre_id=book.genre_id,
        author_id=book.author_id,
    )
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book


def update_book(db: Session, book_id: int, book_update: schemas.BookUpdate):
    db_book = get_book(db, book_id)
    if db_book:
        update_data = book_update.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_book, key, value)
        db.commit()
        db.refresh(db_book)
    return db_book


def delete_book(db: Session, book_id: int):
    db_book = get_book(db, book_id)
    if db_book:
        db.delete(db_book)
        db.commit()
    return db_book
