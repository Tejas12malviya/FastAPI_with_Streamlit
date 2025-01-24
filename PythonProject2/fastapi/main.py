from typing import Annotated

from pydantic import BaseModel,Field
from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends
import models
from database import SessionLocal
from models import Student
from database import engine

app=FastAPI()

models.base.metadata.create_all(bind=engine)

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency=Annotated[Session,Depends(get_db)]

class Student_request(BaseModel):
    name:str
    roll_no:int
    Class:int
    gender:str
    address:str
    math_marks:int=Field(le=100)
    physics_marks:int=Field(le=100)
    chemistry_marks:int=Field(le=100)
    hindi_marks:int=Field(le=100)
    english_marks:int=Field(le=100)

    model_config = {
        'json_schema_extra':{
            'example':{
                'name':'Rohan',
                'roll_no':21,
                'Class':10,
                'gender':'Male',
                'address':'Bhopal',
                'math_marks':98,
                'physics_marks':92,
                'chemistry_marks':89,
                'hindi_marks':77,
                'english_marks':78
            }
        }
    }
@app.get("/")
def read(db:db_dependency):
    return db.query(Student).all()

@app.post("/create")
def create(db:db_dependency,std_new:Student_request):
    std=Student(**std_new.dict())
    db.add(std)
    db.commit()


