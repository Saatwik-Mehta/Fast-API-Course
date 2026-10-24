from sqlalchemy.ext.asyncio import AsyncSession
from .schemas import BookUpdate, BookCreate
from .models import Book
from sqlmodel import select, desc
from datetime import datetime


class BookService:
    async def add_book(self, book_data: BookCreate, session: AsyncSession):
        """Function to add a new Book"""
        body = book_data.model_dump()
        new_book = Book(**body)
        new_book.published_date = datetime.strptime(body["published_date"], "%Y-%m-%d")
        session.add(new_book)
        await session.commit()
        return new_book

    async def fetch_a_book(self, book_id: str, session: AsyncSession):
        """Function to fetch a book data"""
        statement = select(Book).where(Book.id == book_id)
        result = await session.exec(statement)
        return result.first()

    async def update_book_data(
        self, book_id: str, update_data: BookUpdate, session: AsyncSession
    ):
        """Function to update a single book data"""
        book_to_update = await self.fetch_a_book(book_id, session)

        if not book_to_update:
            return None

        update_body = update_data.model_dump()
        for item, updated_val in update_body.items():
            setattr(book_to_update, item, updated_val)

        await session.commit()

        return book_to_update

    async def remove_book(self, book_id: str, session: AsyncSession):
        """Function to remove a single book"""
        book_to_delete = await self.fetch_a_book(book_id, session)

        if not book_to_delete:
            return False

        await session.delete(book_to_delete)
        await session.commit()
        return True

    async def get_all_books(self, session: AsyncSession):
        """Function to fetch all books"""
        statement = select(Book).order_by(desc(Book.created_at))
        result = await session.exec(statement)
        return result.all()
