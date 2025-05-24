from fastapi import FastAPI, Query
from typing import List
import json
import os

app = FastAPI()

# Load data on startup
file_path = os.path.join(os.path.dirname(__file__), "q-vercel-python.json")
with open(file_path, "r") as f:
    student_data = json.load(f)

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/api")
def get_marks(name: List[str] = Query([])):
    name_set = set(name)
    return {"message": "123"}
    # Filter matching names
    # name_to_data = {entry["name"]: entry for entry in student_data}
    # result = [name_to_data[n] for n in name if n in name_to_data]

    # return result
