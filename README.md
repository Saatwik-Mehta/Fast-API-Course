# Bookly - Book Management System API

A modular, lightweight RESTful API for managing books, built using **FastAPI** and **Pydantic**.

---

## 📖 Overview

**Bookly** provides a structured CRUD (Create, Read, Update, Delete) API service for managing a book catalog. It uses FastAPI's modular routing (`APIRouter`) and Pydantic models for request validation and serialization.

---

## ✨ Features

- **CRUD Operations**: Endpoints to create, read, update, and delete books.
- **Modular Architecture**: Clean separation of concerns with dedicated schemas, routes, and data sources.
- **Pydantic Data Validation**: Automatic type validation and partial updates for book records.
- **Interactive Documentation**: Auto-generated Swagger UI (`/docs`) and ReDoc (`/redoc`).
- **RESTful Design**: Versioned endpoints under `/api/v1/books`.

---

## 📁 Project Structure

```text
Bookly/
├── requirements.txt         # Project dependencies
├── README.md                # Project documentation
└── src/
    ├── __init__.py          # FastAPI application initialization & router mounting
    └── books/
        ├── __init__.py
        ├── book_data.py     # In-memory book data store
        ├── routes.py        # APIRouter definitions and route handlers
        └── schemas.py       # Pydantic schemas (Book, BookUpdate)
```

---

## 🛠️ Tech Stack

- **Python 3.10+**
- **FastAPI**
- **Uvicorn** (ASGI web server)
- **Pydantic v2**

---

## 🚀 Getting Started

### Prerequisites

Ensure you have Python 3.10 or higher installed:

```bash
python3 --version
```

### 1. Clone the Repository

```bash
git clone <repository-url>
cd Bookly
```

### 2. Create and Activate a Virtual Environment

- **macOS / Linux**:
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

- **Windows (Command Prompt)**:
  ```cmd
  python -m venv venv
  venv\Scripts\activate.bat
  ```

- **Windows (PowerShell)**:
  ```powershell
  python -m venv venv
  venv\Scripts\Activate.ps1
  ```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ⚡ Running the Application

Start the local development server with live reload:

```bash
uvicorn src:app --reload
```

Alternatively, if you use the FastAPI CLI:

```bash
fastapi dev src/__init__.py
```

The application will start at:
- **Base URL**: `http://127.0.0.1:8000`
- **Interactive API Docs (Swagger UI)**: `http://127.0.0.1:8000/docs`
- **Alternative Docs (ReDoc)**: `http://127.0.0.1:8000/redoc`

---

## 📡 API Endpoints

All endpoints are prefixed with `/api/v1/books`.

| Method | Endpoint | Description | Status Code |
| :--- | :--- | :--- | :--- |
| `GET` | `/api/v1/books/` | Retrieve a list of all books | `200 OK` |
| `POST` | `/api/v1/books/` | Add a new book to the collection | `201 Created` |
| `GET` | `/api/v1/books/{book_id}` | Retrieve details of a specific book by ID | `200 OK` / `404 Not Found` |
| `PUT` | `/api/v1/books/{book_id}` | Update fields of an existing book | `200 OK` / `404 Not Found` |
| `DELETE` | `/api/v1/books/{book_id}` | Delete a book by ID | `204 No Content` / `404 Not Found` |

---

## 💡 Example Usage

### 1. Get All Books
```bash
curl -X GET "http://127.0.0.1:8000/api/v1/books/"
```

### 2. Get a Single Book by ID
```bash
curl -X GET "http://127.0.0.1:8000/api/v1/books/1"
```

### 3. Add a New Book
```bash
curl -X POST "http://127.0.0.1:8000/api/v1/books/" \
     -H "Content-Type: application/json" \
     -d '{
       "id": 11,
       "title": "Fluent Python",
       "author": "Luciano Ramalho",
       "publisher": "O'\''Reilly Media",
       "published_date": "2022-05-01",
       "page_count": 1014,
       "language": "English"
     }'
```

### 4. Update a Book
```bash
curl -X PUT "http://127.0.0.1:8000/api/v1/books/1" \
     -H "Content-Type: application/json" \
     -d '{
       "page_count": 350
     }'
```

### 5. Delete a Book
```bash
curl -X DELETE "http://127.0.0.1:8000/api/v1/books/1"
```
