from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from fastapi_pagination import Page, paginate

from books import crud
from books import schemas
from database import SessionLocal

books_router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@books_router.get("/genres/", response_model=Page[schemas.Genre])
def genres(db: Session = Depends(get_db)):
    db_genres = crud.get_genres(db)
    return paginate(db_genres)


@books_router.get("/genres/{genre_id}", response_model=schemas.Genre)
def read_genre(genre_id: int, db: Session = Depends(get_db)):
    db_genre = crud.get_genre(db, genre_id=genre_id)
    if db_genre is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_genre


@books_router.post("/genres/create", response_model=schemas.Genre)
def create_genre(genre: schemas.GenreCreate, db: Session = Depends(get_db)):
    return crud.create_genre(db=db, genre=genre)


@books_router.put("/genres/{genre_id}", response_model=schemas.Genre)
def update_genre(genre_id: int, genre: schemas.GenreUpdate, db: Session = Depends(get_db)):
    db_genre = crud.update_genre(db, genre_id, genre)
    if db_genre is None:
        raise HTTPException(status_code=404, detail="Author not found")
    return db_genre


@books_router.delete("/genres/{genre_id}", response_model=schemas.Genre)
def delete_genre(genre_id: int, db: Session = Depends(get_db)):
    db_genre = crud.delete_genre(db, genre_id)
    if db_genre is None:
        raise HTTPException(status_code=404, detail="Genre not found")
    return db_genre


@books_router.get("/authors/", response_model=Page[schemas.Author])
def authors(db: Session = Depends(get_db)):
    db_authors = crud.get_authors(db)
    return paginate(db_authors)


@books_router.get("/authors/{author_id}", response_model=schemas.Author)
def read_author(author_id: int, db: Session = Depends(get_db)):
    db_author = crud.get_author(db, author_id=author_id)
    if db_author is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_author


@books_router.post("/authors/create", response_model=schemas.Author)
def create_author(author: schemas.AuthorCreate, db: Session = Depends(get_db)):
    return crud.create_author(db=db, author=author)


@books_router.put("/authors/{author_id}", response_model=schemas.Author)
def update_author(author_id: int, author_update: schemas.AuthorUpdate, db: Session = Depends(get_db)):
    db_author = crud.update_author(db, author_id, author_update)
    if db_author is None:
        raise HTTPException(status_code=404, detail="Author not found")
    return db_author


@books_router.delete("/authors/{author_id}", response_model=schemas.Author)
def delete_author(author_id: int, db: Session = Depends(get_db)):
    db_author = crud.delete_author(db, author_id)
    if db_author is None:
        raise HTTPException(status_code=404, detail="Author not found")
    return db_author


@books_router.get("/books/", response_model=Page[schemas.Book])
def books(db: Session = Depends(get_db)):
    db_books = crud.get_books(db)
    return paginate(db_books)


@books_router.get("/books/{book_id}", response_model=schemas.Book)
def read_book(book_id: int, db: Session = Depends(get_db)):
    db_book = crud.get_book(db, book_id=book_id)
    if db_book is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_book


@books_router.post("/books/create", response_model=schemas.Book)
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    return crud.create_book(db=db, book=book)


@books_router.put("/books/{book_id}", response_model=schemas.Book)
def update_book(book_id: int, book_update: schemas.BookUpdate, db: Session = Depends(get_db)):
    db_book = crud.update_book(db, book_id, book_update)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Author not found")
    return db_book


@books_router.delete("/books/{book_id}", response_model=schemas.Book)
def delete_book(book_id: int, db: Session = Depends(get_db)):
    db_book = crud.delete_book(db, book_id)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book
