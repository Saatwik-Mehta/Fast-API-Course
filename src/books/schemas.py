from pydantic import BaseModel
from typing import Optional
from uuid import UUID, uuid4
from datetime import datetime

class Book(BaseModel):
    id: UUID
    title: str
    language: str
    author: str
    publisher: str
    published_date: str
    page_count: int
    created_at: datetime
    updated_at: datetime
    created_by: str
    updated_by: str


class BookCreate(BaseModel):
    title: str
    language: str
    author: str
    publisher: str
    page_count: int
    published_date: str
    created_at: datetime
    created_by: str


class BookUpdate(BaseModel):
    title: Optional[str] = None
    language: Optional[str] = None
    author: Optional[str] = None
    publisher: Optional[str] = None
    published_date: Optional[str] = None
    page_count: Optional[int] = None
    updated_at: Optional[datetime] = None
    updated_by: Optional[str] = None
    
