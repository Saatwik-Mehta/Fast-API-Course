from sqlalchemy.ext.asyncio import AsyncSession
from .schemas import BookUpdate, BookCreate

class BookService:
    async def add_book(self, book_data: BookCreate, session: AsyncSession):
        pass
    async def updata_book_data(self, book_id: str, update_data: BookUpdate, session: AsyncSession):
        pass
    async def remove_book(self, book_id: str, session: AsyncSession):
        pass
    async def fetch_a_book(self, book_id: str, session: AsyncSession):
        pass
    async def get_all_books(self, session: AsyncSession):
        pass