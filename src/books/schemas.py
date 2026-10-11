from pydantic import BaseModel
from typing import Optional

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
