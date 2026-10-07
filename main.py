from typing import Dict, List, Optional
from artifacts import books
from fastapi import FastAPI, status
from fastapi.exceptions import HTTPException
from pydantic import BaseModel

app = FastAPI()


class Book(BaseModel):
    id: int
    title: str
    language: str
    author: str
    publisher: str
    published_date: str
    page_count: int


class BookUpdate(BaseModel):
    title: Optional[str] = None
    language: Optional[str] = None
    author: Optional[str] = None
    publisher: Optional[str] = None
    page_count: Optional[int] = None


@app.post("/book", status_code=status.HTTP_201_CREATED)
def add_book(book_data: Book) -> Dict:
    new_book = book_data.model_dump()
    books.append(new_book)
    return new_book


@app.put("/book/{book_id}", status_code=200)
def update_book(book_id: int, updated_data: BookUpdate) -> Dict:
    for book in books:
        if book["id"] == book_id:
            book.update(updated_data.model_dump())
            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")


@app.get("/book/{book_id}", status_code=200)
def get_a_book(book_id: int) -> Dict:
    for book in books:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")


@app.get("/books", status_code=200, response_model=List[Book])
def all_books() -> Dict:
    return books


@app.delete("/book/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            return {}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
