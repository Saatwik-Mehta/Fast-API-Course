from pydantic import BaseModel
from typing import Optional
from uuid import UUID, uuid4
from datetime import datetime, date


class Book(BaseModel):
    id: UUID
    title: str
    language: str
    author: str
    publisher: str
    published_date: date
    page_count: int
    created_at: datetime
    created_by: UUID


class BookCreate(BaseModel):
    title: str
    language: str
    author: str
    publisher: str
    page_count: int
    published_date: str
    created_by: str


class BookUpdate(BaseModel):
    title: str
    language: str
    author: str
    publisher: str
    page_count: int
    updated_by: str
