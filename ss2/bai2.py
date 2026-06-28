from fastapi import FastAPI

app = FastAPI()

students = [
    {"id": 1, "name": "An"},
    {"id": 2, "name": "Binh"},
    {"id": 3, "name": "Cuong"},
]

# P1
# 1/student

# 2 gọi /students mà chỉ có student, không tìm thấy 404

# 3 phải dùng students thay vì student

# 5 Là: /students

@app.get("/students")
def get_students():
    return students