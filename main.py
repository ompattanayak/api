# main.py
from fastapi import FastAPI, Request
from typing import List
from fastapi.responses import JSONResponse
import json

app = FastAPI()

# Load JSON data once when the app starts
with open("q-vercel-python.json", "r") as file:
    student_data = json.load(file)

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/api")
def get_marks(name: List[str] = []):
    name_set = set(name)
    filtered_students = [entry for entry in student_data if entry["name"] in name_set]
    
    # Maintain the order from query
    ordered_result = [next(item for item in filtered_students if item["name"] == n) for n in name if any(item["name"] == n for item in filtered_students)]

    return JSONResponse(content=ordered_result)
