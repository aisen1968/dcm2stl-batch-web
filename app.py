from fastapi import FastAPI
from fastapi.responses import FileResponse
import os

app = FastAPI(title="DCM to STL Converter")

@app.get("/")
async def root():
    return {"message": "Welcome to DCM to STL Converter"}

@app.get("/health")
async def health():
    return {"status": "ok"}
