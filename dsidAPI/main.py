from typing import List, Union, Optional

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import readOperations, dataModels, schemas
from .database import SessionLocal, dbEngine

dataModels.Base.metadata.create_all(bind=dbEngine)

app = FastAPI()

## Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/Ingredients/")
def read_users(name: str, db: Session = Depends(get_db)):
    ingredient = readOperations.get_ingredient(db, name)
    
    #if id :
    #    ingredient.update(id = id)
    return ingredient

## Default list of most common ingredients

@app.get("/children_1to4/", response_model = List[schemas.defaultResults])
def default_results(ingredient : Optional[str] = None, label : Optional[float] = None, db: Session = Depends(get_db)):
    allResults = readOperations.getAllDefault(product = 6, ingredient = ingredient, label = label, db = db)

    return allResults

@app.get('/test/')
def SomeResult(db: Session = Depends(get_db)):

    return readOperations.getSomeResult(db = db)