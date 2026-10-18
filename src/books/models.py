from sqlmodel import SQLModel, Field, Column
import sqlalchemy.dialects.postgresql as pg
from typing import Optional
from datetime import datetime
from uuid import UUID, uuid4


class Book(SQLModel, table=True):
    id: UUID = Field(
        sa_column=Column(pg.UUID, nullable=False, primary_key=True, default=uuid4)
    )
    title: str
    language: str
    author: str
    publisher: str
    published_date: str
    page_count: int
    created_at: Optional[datetime] = Field(sa_column=Column(pg.TIMESTAMP, default=datetime.now))
    updated_at: Optional[datetime] = None
    created_by: Optional[str] = Field(sa_column=Column(pg.UUID, nullable=False, default=uuid4))
    updated_by: Optional[str] = None

    def __repr__(self):
        return f"<Book {self.title}>"


class BookUpdate(SQLModel):
    title: Optional[str] = None
    language: Optional[str] = None
    author: Optional[str] = None
    publisher: Optional[str] = None
    page_count: Optional[int] = None
    updated_at: Optional[datetime] = Field(sa_column=Column(pg.TIMESTAMP, default=datetime.now))
    updated_by: Optional[str] = Field(sa_column=Column(pg.UUID, nullable=True, default=uuid4))
