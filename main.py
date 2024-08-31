from fastapi import FastAPI

from books.router import books_router
from fastapi_pagination import add_pagination

app = FastAPI()

app.include_router(books_router)
add_pagination(app)
