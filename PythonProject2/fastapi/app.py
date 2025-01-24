import streamlit as st
import requests
from pydantic import BaseModel,Field


class Student_request(BaseModel):
    name: str
    roll_no: int
    Class: int
    gender: str
    address: str
    math_marks: int = Field(le=100)
    physics_marks: int = Field(le=100)
    chemistry_marks: int = Field(le=100)
    hindi_marks: int = Field(le=100)
    english_marks: int = Field(le=100)


st.title("Student Management")
with st.form("student_form"):
    st.header("Add New Student")
    name = st.text_input("Name")
    roll_no = st.number_input("Roll No.", min_value=1)
    class_ = st.number_input("Class", min_value=1)
    gender = st.selectbox("Gender", ("Male", "Female", "Other"))
    address = st.text_input("Address")
    math_marks = st.number_input("Math Marks", min_value=0, max_value=100)
    physics_marks = st.number_input("Physics Marks", min_value=0, max_value=100)
    chemistry_marks = st.number_input("Chemistry Marks", min_value=0, max_value=100)
    hindi_marks = st.number_input("Hindi Marks", min_value=0, max_value=100)
    english_marks = st.number_input("English Marks", min_value=0, max_value=100)

    if st.form_submit_button("Submit"):
        try:
            student_data = {
                "name": name,
                "roll_no": roll_no,
                "Class": class_,
                "gender": gender,
                "address": address,
                "math_marks": math_marks,
                "physics_marks": physics_marks,
                "chemistry_marks": chemistry_marks,
                "hindi_marks": hindi_marks,
                "english_marks": english_marks
            }

            response = requests.post("http://localhost:8000/create", json=student_data)
            response.raise_for_status()  # Raise an exception for bad status codes

            st.success("Student added successfully!")

        except requests.exceptions.RequestException as e:
            st.error(f"Error creating student: {e}")

try:
    response = requests.get("http://localhost:8000/")
    response.raise_for_status()
    students = response.json()
    st.subheader("Existing Students")
    st.table(students)

except requests.exceptions.RequestException as e:
    st.error(f"Error fetching students: {e}")




