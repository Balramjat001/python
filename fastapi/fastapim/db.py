from fastapi import FastAPI
from classapi import data

app = FastAPI()

@app.get("/data")
def abb():
    return data
