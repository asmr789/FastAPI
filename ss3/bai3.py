from fastapi import FastAPI

app = FastAPI()

books = [
    {
        "id": 1,
        "title": "Python Basic",
        "author": "Nguyen Van A",
        "category": "programming",
        "year": 2022,
        "is_available": True
    },
    {
        "id": 2,
        "title": "Web API Design",
        "author": "Tran Van B",
        "category": "web",
        "year": 2021,
        "is_available": False
    },
    {
        "id": 3,
        "title": "Database System",
        "author": "Le Minh Huyen",
        "category": "database",
        "year": 2020,
        "is_available": True
    },
    {
        "id": 4,
        "title": "Clean Code",
        "author": "Le Anh Linh",
        "category": "programming",
        "year": 2008,
        "is_available": False
    },
    {
        "id": 5,
        "title": "Computer Network",
        "author": "Vu Hong Van",
        "category": "network",
        "year": 2019,
        "is_available": True
    }
]

@app.get("/books/statistics")
def get_statistics():
    total_books = len(books)
    available_books = len([b for b in books if b["is_available"]])
    borrowed_books = len([b for b in books if not b["is_available"]])
    return {
        "total_books": total_books,
        "available_books": available_books,
        "borrowed_books": borrowed_books
    }

@app.get("/books/categories")
def get_categories():
    categories = list(set([b["category"] for b in books]))
    return {"categories": categories}

@app.get("/books/latest")
def get_latest_book():
    if not books:
        return {"message": "No books available"}
    latest_book = max(books, key=lambda b: b["year"])
    return latest_book
