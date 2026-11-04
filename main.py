from fastapi import FastAPI
from database import engine, Base
from model.student import Student
from router import student

app = FastAPI(
    title = "Student Project",
    summary = "RESTAPI project with db integrated"
)

Base.metadata.create_all(bind = engine)

app.include_router(student.router)

@app.get("/")
def home():
    return {
        "message" : "Student Mangement API is running"
    }