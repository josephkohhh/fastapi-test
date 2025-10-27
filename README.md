This repo contains source code for fastapi-test, a simple backend CRUD app

## Table of Contents

- [Instructions](#Instructions)
- [App Structure](#AppStructure)
- [Features](#Features)

## Instruction

- 1. setup folder and .gitignore
- 2. install virtualenv
  - python3 -m venv myenv
- 3. myenv\Scripts\Activate.ps1 / source myenv/bin/activate
  - ensure python interpretor is now pointing to myenv
- 4. install fastapi and uvicorn
  - pip install fastapi
  - pip install uvicorn
- 5. run server
  - uvicorn main:app --reload

## App Structure

```
app/
├── main.py # FastAPI app and routes (entry point)
├── database.py # DB connection setup (SQLAlchemy engine & session)
├── models.py # SQLAlchemy ORM models (table definitions)
├── schemas.py # Pydantic models for request/response validation
└── crud.py # CRUD functions (create/read/update/delete)
```

## Features

- Fetch all
- Fetch by id
- Create
- Update
- Delete
