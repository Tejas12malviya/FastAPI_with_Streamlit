from database import base
from sqlalchemy import Column, Integer, String

class Student(base):
    __tablename__='student'

    id=Column(Integer,primary_key=True,index=True)
    name=Column(String)
    roll_no=Column(Integer)
    Class=Column(Integer)
    gender=Column(String)
    address=Column(String)
    math_marks=Column(Integer)
    physics_marks=Column(Integer)
    chemistry_marks=Column(Integer)
    hindi_marks=Column(Integer)
    english_marks=Column(Integer)
