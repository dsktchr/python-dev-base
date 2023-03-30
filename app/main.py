from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from this import d

import crud
import models
import schemas

from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered.")
    return crud.create_user(db=db, user=user)


@app.get("/users/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 0, db: Session = Depends(get_db)):
    users = crud.get_users(db=db, skip=skip, limit=limit)
    return users


@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db=db, user_id=user_id)
    if db_user:
        raise HTTPException(status_code=404, detail="User not found.")
    return db_user


@app.post("/users/{user_id}/items/", response_model=schemas.Item)
def create_item_for_user(
    user_id, item: schemas.ItemCreate, db: Session = Depends(get_db)
):
    return crud.create_user_items(db=db, item=item, user_id=user_id)


@app.get("/items/")
def read_item(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_items(db=db, skip=skip, limit=limit)
    return items


@app.get("/")
def read_root():
    return {"Hello", "World"}


@app.get("/items/{item_id}")
def read_items(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}


fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/qitems/")
def read_qitems(skip: int = 0, limit: int = 0):
    return fake_items_db[skip : skip + limit]
