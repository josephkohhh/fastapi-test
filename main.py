# main.py - FastAPI app and routes

# myenv\Scripts\Activate.ps1 source myenv/bin/activate
# uvicorn main:app --reload

from fastapi import FastAPI
import models
from database import engine

app = FastAPI() # Instantiate FastAPI class

@app.get('/')
def homepage():
    return 'Go to /docs to test this API'


models.Base.metadata.create_all(bind=engine) # Create tables in db defined in models.py


