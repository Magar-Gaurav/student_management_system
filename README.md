# Student Management API

A RESTful Student Management API built using **FastAPI, PostgreSQL, SQLAlchemy, and Pydantic**.

This project demonstrates backend development concepts, including CRUD operations, database integration, request validation, response serialization, dependency injection, and error handling.

## Features

- Create new student records.
- Retrieve all students.
- Retrieve an individual student by ID.
- Update student information.
- Delete student records.
- Validate incoming data using Pydantic.
- Serialize database objects using response models.
- Connect to PostgreSQL using SQLAlchemy.
- Manage database sessions using FastAPI dependency injection.
- Handle errors using HTTP exceptions.
- Use appropriate HTTP status codes.

## Tech Stack

| Technology | Purpose |
|---|---|
| Python | Programming language |
| FastAPI | Backend API framework |
| PostgreSQL | Relational database |
| SQLAlchemy | ORM and database operations |
| Pydantic | Data validation and serialization |
| Uvicorn | ASGI server |

## Project Structure

```text
student_management_api/
│
├── model/
│   └── student.py
│
├── router/
│   └── student.py
│
├── schemas/
│   └── student.py
│
├── database.py
├── main.py
├── requirements.txt
├── .env
└── .gitignore
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/student-management-api.git
```

### 2. Navigate into the project

```bash
cd student-management-api
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Configure environment variables

Create a `.env` file in the root directory:

```env
DATABASE_URL=postgresql+psycopg://username:password@localhost:5432/database_name
```

Replace the username, password, and database name with your PostgreSQL credentials.

Make sure PostgreSQL is running and the database exists before starting the application.

### 7. Run the application

```bash
uvicorn main:app --reload
```

## API Endpoints

Base URL:

```text
http://127.0.0.1:8000
```

| Method | Endpoint | Description |
|---|---|---|
| POST | `/students/` | Create a student |
| GET | `/students/` | Get all students |
| GET | `/students/{student_id}` | Get a student by ID |
| PUT/PATCH | `/students/{student_id}` | Update student information |
| DELETE | `/students/{student_id}` | Delete a student |

Use the update method implemented in your project (PUT or PATCH).

## API Documentation

After starting the server, access the interactive API documentation:

- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

You can use these interfaces to test the API endpoints.

## Learning Outcomes

Through this project, I practised:

- Building RESTful APIs using FastAPI.
- Working with relational databases.
- Performing CRUD operations using SQLAlchemy.
- Understanding dependency injection.
- Managing database sessions.
- Validating request data with Pydantic.
- Handling HTTP exceptions and status codes.
- Structuring a backend application into separate modules.

## Future Improvements

- Authentication and authorization.
- Pagination and filtering.
- Automated testing with Pytest.
- Docker deployment.
- API deployment to a cloud platform.


*Built as a hands-on backend development learning project.*
