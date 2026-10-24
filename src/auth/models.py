from datetime import datetime
from uuid import UUID, uuid4
from sqlmodel import SQLModel, Field, Column
import sqlalchemy.dialects.postgresql as pg



class Users(SQLModel, table=True):
    __tablename__ = "users"
    user_id: UUID = Field(sa_column=Column(pg.UUID, nullable=False, primary_key=True, default=uuid4))
    username: str
    email_id: str
    first_name: str
    last_name: str
    is_verified: bool = Field(default=False)
    created_at: datetime = Field(sa_column=Column(pg.TIMESTAMP, default=datetime.now))
    updated_at: datetime = Field(sa_column=Column(pg.TIMESTAMP, default=None))

    def __repr__(self):
        return f"<User {self.username}>"