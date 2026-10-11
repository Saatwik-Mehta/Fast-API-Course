from typing import List, Dict

from fastapi import APIRouter, status
from fastapi.exceptions import HTTPException
from src.books.schemas import Book, BookUpdate
from src.books.book_data import books

books_routes = APIRouter()



@books_routes.post("/", status_code=status.HTTP_201_CREATED)
def add_book(book_data: Book) -> Dict:
    new_book = book_data.model_dump()
    books.append(new_book)
    return new_book


@books_routes.put("/{book_id}", status_code=200)
def update_book(book_id: int, updated_data: BookUpdate) -> Dict:
    for book in books:
        if book["id"] == book_id:
            book.update(updated_data.model_dump())
            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")


@books_routes.get("/{book_id}", status_code=200)
def get_a_book(book_id: int) -> Dict:
    for book in books:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")


@books_routes.get("/", status_code=200, response_model=List[Book])
def all_books() -> Dict:
    return books


@books_routes.delete("/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            return {}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
