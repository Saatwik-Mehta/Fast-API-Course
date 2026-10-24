from sqlmodel import SQLModel, Field, Column
import sqlalchemy.dialects.postgresql as pg
from typing import Optional
from datetime import datetime, date
from uuid import UUID, uuid4


class Book(SQLModel, table=True):
    id: UUID = Field(
        sa_column=Column(pg.UUID, nullable=False, primary_key=True, default=uuid4)
    )
    title: str
    language: str
    author: str
    publisher: str
    published_date: date
    page_count: int
    created_at: Optional[datetime] = Field(
        sa_column=Column(pg.TIMESTAMP, default=datetime.now)
    )
    updated_at: Optional[datetime] = None
    created_by: Optional[str] = Field(
        sa_column=Column(pg.UUID, nullable=False, default=None)
    )
    updated_by: Optional[str] = None

    def __repr__(self):
        return f"<Book {self.title}>"
