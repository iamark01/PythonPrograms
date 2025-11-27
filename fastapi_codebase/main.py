import os
import uvicorn
import shutil

from fastapi import FastAPI, File, UploadFile, Request
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi import Form
from typing import List
from pydantic import BaseModel, Field
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

app = FastAPI()

templates = Jinja2Templates(directory=str(Path(BASE_DIR,'templates')))

app.mount("/static",StaticFiles(directory=str(Path(BASE_DIR,'static'))), name="static")

class Student(BaseModel):
   id: int
   name :str = Field(title="name of student", max_length=10)
   subjects: List[str] = []

class User(BaseModel):
   username: str
   password: str

@app.post("/students/{college}")
async def student_data(college:str, age:int, student:Student):
   retval = {"college":college, "age":age, **student.model_dump()}
   return retval

@app.get("/")
async def index():
   return {"message": "Hello World"}

@app.get("/hello/{name}", response_class=HTMLResponse)
async def hello(request : Request, name: str):
   return templates.TemplateResponse("hello.html",{"request": request,"name": name})

@app.get("/login/", response_class=HTMLResponse)
async def login(request: Request):
   return templates.TemplateResponse("login.html", {"request": request})

@app.post("/submit/", response_model=User)
async def submit(username: str=Form(max_length=30, description="Username"), password: str=Form(max_length=10, description="Password")):
   return User(username=username, password=password)

@app.get("/upload/", response_class=HTMLResponse)
async def upload(request: Request):
   return templates.TemplateResponse("uploadfile.html", {"request": request})

@app.post("/uploader/")
async def create_upload_file(file: UploadFile = File()):
   try:
      file_path = f"{BASE_DIR}{os.sep}static{os.sep}{file.filename}"
      with open(file_path, "wb") as buffer:
         shutil.copyfileobj(file.file, buffer)
      return {"filename": file.filename}
   except Exception as e:
      return {"message": e.args}

@app.get("/fileslist/")
async def list_files(request: Request):
   try:
      files_dir = f"{BASE_DIR}{os.sep}static{os.sep}"
      file_list = [f for f in os.listdir(files_dir) if os.path.isfile(os.path.join(files_dir, f))]
      return templates.TemplateResponse("files.html", {"request": request, "files": file_list})
   except Exception as e:
      return {"message": e.args}

@app.get("/fileslist/{name}")
async def read_item(request: Request, name: str):
   try:
      file_path = f"{BASE_DIR}{os.sep}static{os.sep}{name}"
      return FileResponse(file_path, media_type='application/octet-stream', filename=name)
   except Exception as e:
      return {"message": e.args}

if __name__ == "__main__":
   uvicorn.run("main:app", host="localhost", port=8000, reload=True)