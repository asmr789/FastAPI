from fastapi import FastAPI

app = FastAPI()

books = [
    {"id": 1,"title": "Python Basic","author": "Nguyen Van A","category": "programming","year": 2022,"is_available": True},
    {"id": 2,"title": "Web API Design","author": "Tran Van B","category": "web","year": 2021,"is_available": False},
    {"id": 3,"title": "Database System","author": "Le Minh Huyen","category": "database","year": 2020,"is_available": True},
    {"id": 4,"title": "Clean Code","author": "Le Anh Linh","category": "programming","year": 2008,"is_available": False},
    {"id": 5,"title": "Computer Network","author": "Vu Hong Van","category": "network","year": 2019,"is_available": True}
]

@app.get("/books/available")
def get_available_books():
    result = [book for book in books if book["is_available"] == True]
    return result

@app.get("/books/borrowed")
def get_borrowed_books():
    result = [book for book in books if book["is_available"] == False]
    return result
