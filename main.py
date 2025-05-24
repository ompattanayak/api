from fastapi import FastAPI, Query
from typing import List
import json
import os

app = FastAPI()

# Load JSON data on startup
file_path = os.path.join(os.path.dirname(__file__), "q-vercel-python.json")
with open(file_path, "r") as f:
    student_data = json.load(f)

# Create a name -> marks mapping for faster lookup
name_to_marks = {entry["name"]: entry["marks"] for entry in student_data}

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/api")
def get_marks(name: List[str] = Query([])):
    # Extract marks in the order of names passed
    marks = [name_to_marks[n] for n in name if n in name_to_marks]
    return {"marks": marks}
