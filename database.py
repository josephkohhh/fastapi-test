# database.py - db connection setup (SQLAlchemy engine & session)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv # pip install python-dotenv
import os

load_dotenv()  # Load .env file
db_url = os.getenv("DATABASE_URL")

engine = create_engine(db_url) # To tell app where and how to connect to db
session = sessionmaker(autocommit=False,autoflush=True,bind=engine) # To connect to db

