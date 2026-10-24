from typing import List, Dict
from uuid import UUID
from fastapi import APIRouter, status, Depends
from fastapi.exceptions import HTTPException
from src.books.schemas import BookCreate, BookUpdate, Book
from src.books.service import BookService
from src.db.main import get_session
from sqlmodel.ext.asyncio.session import AsyncSession

books = BookService()
books_routes = APIRouter()


@books_routes.post("/", status_code=status.HTTP_201_CREATED, response_model=Book)
async def add_book(
    book_data: BookCreate, session: AsyncSession = Depends(get_session)
) -> Dict:
    new_book = await books.add_book(book_data, session)
    print(new_book)
    return new_book


@books_routes.put("/{book_id}", status_code=status.HTTP_200_OK, response_model=Book)
async def update_book(
    book_id: UUID,
    updated_data: BookUpdate,
    session: AsyncSession = Depends(get_session),
) -> Dict:
    updated_book = await books.update_book_data(book_id, updated_data, session)
    if not updated_data:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Book not found"
        )
    return updated_book


@books_routes.get("/{book_id}", status_code=status.HTTP_200_OK, response_model=Book)
async def get_a_book(
    book_id: UUID, session: AsyncSession = Depends(get_session)
) -> Dict:
    book = await books.fetch_a_book(book_id, session)
    if not book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Book not found"
        )
    return book


@books_routes.get("/", status_code=status.HTTP_200_OK, response_model=List[Book])
async def all_books(session: AsyncSession = Depends(get_session)) -> Dict:
    all_books = await books.get_all_books(session)
    if not all_books:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="No available books!"
        )
    return all_books


@books_routes.delete("/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: UUID, session: AsyncSession = Depends(get_session)):
    deleted_book = await books.remove_book(book_id, session)
    if not deleted_book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Book not found"
        )
