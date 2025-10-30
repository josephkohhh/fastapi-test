# main.py - FastAPI app and routes

# python3 -m venv myenv
# myenv\Scripts\Activate.ps1 source myenv/bin/activate
# uvicorn main:app --reload

from fastapi import FastAPI, Depends
import models 
import database
from sqlalchemy.orm import Session
import crud
import schemas

app = FastAPI() # Instantiate FastAPI class

models.Base.metadata.create_all(bind=database.engine) # Create tables in db defined in models.py

@app.get('/')
def homepage():
    return 'Go to /docs to test this API'


@app.get('/user')
def read_users(db: Session = Depends(database.get_db)):
    return crud.get_all_user(db)


@app.get('/user/{id}')
def read_user_by_id(id: int, db: Session = Depends(database.get_db)):
    return crud.get_user_by_id(id, db)


@app.post('/user')
def add_user(user: schemas.UserCreate, db: Session = Depends(database.get_db)):
    return crud.create_user(user, db) 


@app.put('/user')
def modify_user(id: int, user: schemas.UserCreate, db: Session = Depends(database.get_db)):
    return crud.update_user(id, user, db)


@app.delete('/user')
def remove_user(id: int, db: Session = Depends(database.get_db)):
     return crud.delete_user(id, db)





