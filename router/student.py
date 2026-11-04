from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from model.student import Student
from schemas.student import StudentCreate, StudentUpdate, StudentResponse
from sqlalchemy import select

router = APIRouter(
    prefix = "/students",
    tags = ["Students"]
)

@router.post("/", response_model = StudentResponse, status_code = 201)
def create_student(student : StudentCreate, db : Session = Depends(get_db)):
    new_student = Student(
        name = student.name,
        age = student.age,
        rank = student.rank,
        email = student.email
    )

    db.add(new_student)
    db.commit()
    db.refresh(new_student)

    return new_student

@router.get("/", response_model = list[StudentResponse], status_code = 200)
def get_students(db : Session = Depends(get_db)):
    statement = select(Student)

    students = db.scalars(statement).all()

    return students 

@router.get("/{student_id}", response_model = StudentResponse, status_code = 200)
def get_student(student_id : int, db : Session = Depends(get_db)):
    statement = select(Student).where(Student.id == student_id)

    student = db.scalar(statement)

    if student is None:
        raise HTTPException(status_code = 404, detail = "Stduent record not found")
    
    return student

@router.put("/{student_id}", response_model = StudentResponse, status_code = 200)
def update_student(student_id : int, student_data : StudentUpdate, db : Session = Depends(get_db)):
    statement = select(Student).where(Student.id == student_id)

    student = db.scalar(statement)

    if student is None:
        raise HTTPException(status_code = 404, detail = "Stduent record not found")
    
    update_data = student_data.model_dump(
        exclude_unset = True, exclude_none = True
    )

    for key, value in update_data.items():
        setattr(student, key, value)

    db.commit()
    db.refresh(student)

    return student

@router.delete("/{student_id}", status_code = 200)
def delete_student(student_id : int, db : Session = Depends(get_db)):
    statement = select(Student).where(Student.id == student_id)

    student = db.scalar(statement)

    if student is None:
        raise HTTPException(status_code = 404, detail = "Student record not found")

    db.delete(student)
    db.commit()

    return{
        "message" : "Student deleted successfully"
    }