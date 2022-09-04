from typing import Optional
from fastapi import FastAPI, Path
from pydantic import BaseModel

app = FastAPI()

student = {
    1: {
        "name":"gokul","age":23,"year":12
    }
}

#models
#data's storing now as like temp, so whenever we refresh the browser the data created using method will get lost.
class student_model(BaseModel):
    name: str
    age: int
    year: int

class update_student_model(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    year: Optional[int] = None

#get method
@app.get('/')
def index():
    return {"Hey":"You"}

@app.get("/student/{student_id}")  #get details by id
def get_student(student_id:int = Path(None, description="ID of student", gt=0,lt=10)):
    if student_id not in student:
        return {"Error":"ID does't exists"}
    return student[student_id]


@app.get("/get-by-name") #get by student name
def get_student_name(name:str = Path(None, description="Name of student")):
    for stu in student:
        if student[stu]["name"] == name:
            return student[stu]
    return {"Error":"no data"}

#create method
@app.post("/create_student/{student_id}")
def create_student(student_id: int, model: student_model):
    if student_id in student:
        return {"Error":"ID already exists"}

    student[student_id] = model
    return student[student_id]

#update method
@app.put("/update_student/{student_id}")
def update_student(student_id:int, model:update_student_model):
    if student_id not in student:
        return {"Error":"ID doesn't exist"} 

    if model.name != None:
        student[student_id].name = model.name
        
    if model.age != None:
        student[student_id].age = model.age
    
    if model.year != None:
        student[student_id].year = model.year

    student[student_id] == model
    return student[student_id]

#delete method
@app.delete("/delete/{student_id}")
def delete_student(student_id:int):
    if student_id not in student:
        return {"Error":"ID doesn't exists"}
    
    del student[student_id]
    return {"Message":"Student Deleted Successfully"}
    
