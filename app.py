from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Demo FastAPI")


class PredictRequest(BaseModel):
    x: float
    y: float


class PredictResponse(BaseModel):
    sum: float
    product: float


@app.get("/")
def root():
    return {"status": "ok", "message": "FastAPI is running"}


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.post("/predict", response_model=PredictResponse)
def predict(req: PredictRequest):
    return PredictResponse(sum=req.x + req.y, product=req.x * req.y)

# Run command: python3 -m uvicorn main:app --reload --port 8001