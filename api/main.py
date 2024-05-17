from fastapi import FastAPI
import uvicorn

app=FastAPI()

students=[{
    "id":1,
    "name":"Ali"
},
          {
    "id":2,
    "name":"Fahad"
}]

@app.get("/students")
def getstudents():
    return students

@app.post("/addstudents")
def addstudents(id:int,user:str):
    global students
    students.append({"id":3,"name":"Ahmed"})
    return students

@app.put("/updatestudent/{id}")
def updatestudent(id:int):
    global students
    for i in students:
        if i["id"]==id:
            return students
        
@app.delete("/deletestudent/{name}")
def deletestudent(name:str):
    global students
    for i in students:
        if i["name"]==name:
            students.remove(i)
            return students



def start():
    uvicorn.run("todos.main:app", host="127.0.0.1", port=8000, reload=True)
