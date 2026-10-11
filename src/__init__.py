from fastapi import FastAPI
from src.books.routes import books_routes

version = "v1"

app = FastAPI(
    version = version,
    title="Book Management System",
    description="API for managing books",
    docs_url="/docs",
    redoc_url="/redoc"
)

app.include_router(books_routes, prefix=f"/api/{version}/books")