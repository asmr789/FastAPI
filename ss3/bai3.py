from fastapi import FastAPI

app = FastAPI()

products = [
    {"id": 1, "name": "Laptop", "price": 15000000},
    {"id": 2, "name": "Mouse", "price": 200000},
    {"id": 3, "name": "Keyboard", "price": 500000},
    {"id": 4, "name": "Monitor", "price": 3000000}
]

@app.get("/products/search/{name}")
def search_products(name: str):
    filtered = [p for p in products if name.lower() in p["name"].lower()]
    return filtered if filtered else {"message": "không tìm thấy sản phẩm"}

@app.get("/products/price/{max_price}")
def get_products_by_price(max_price: float):
    if max_price < 0:
        return {"message": "không được âm"}
    filtered = [p for p in products if p["price"] <= max_price]
    return filtered if filtered else {"message": "không có sản phẩm phù hợp"}