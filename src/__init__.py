from src.db.main import init_db
from fastapi import FastAPI
from src.books.routes import books_routes
from contextlib import asynccontextmanager

version = "v1"


@asynccontextmanager
async def life_span(app: FastAPI):
    print("Starting the DB....")
    await init_db()
    yield
    print("Stopping the DB....")


app = FastAPI(
    version=version,
    title="Book Management System",
    description="API for managing books",
    docs_url="/docs",
    redoc_url="/redoc",
    lifespan=life_span
)

app.include_router(books_routes, prefix=f"/api/{version}/books")
