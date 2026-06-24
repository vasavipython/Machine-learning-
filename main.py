from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Numbers(BaseModel):
    a: int
    b: int

@app.get("/")
def home():
    return {"message": "Hello FastAPI!"}

@app.get("/add")
def add(a: int, b: int):
    return {"sum": a + b}

@app.post("/multiply")
def multiply(nums: Numbers):
    return {"product": nums.a * nums.b}
