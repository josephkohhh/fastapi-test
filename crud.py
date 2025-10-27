# crud.py - CRUD functions (interacting with models.py)

from sqlalchemy.orm import Session
import models
import schemas 


def get_all_user(db: Session):
    return db.query(models.User).all()


def get_user_by_id(id: int, db: Session):
    db_user = db.query(models.User).filter(models.User.id == id).first()
    if db_user:
        return db_user
    return 'user not found'


def create_user(user: schemas.UserCreate, db: Session):
    db_user = models.User(**user.model_dump())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def update_user(id: int, user: schemas.UserCreate, db: Session):
    db_user = db.query(models.User).filter(models.User.id == id).first()
    if db_user:
        db_user.name = user.name
        db_user.age = user.age
        db_user.married = user.married
        db.commit()
    else:
        return 'no user found'


def delete_user(id: int, db: Session):
    db_user = db.query(models.User).filter(models.User.id == id).first()
    if db_user:
        db.delete(db_user)
        db.commit()
    else:
        return 'no product found'
    
