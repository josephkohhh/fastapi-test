# models.py - SQLAlchemy ORM models (tables)

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean

Base = declarative_base() # Instantiate base class

class User(Base):

    __tablename__ = 'user' # db table name

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    age = Column(Integer)
    married = Column(Boolean)

