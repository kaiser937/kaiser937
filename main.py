from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/tarea-1")
async def read_tarea_1():
    return {"respuesta": "Primer tarea realizada"}

class Tarea_2(BaseModel):
    Prenda:str

@app.post("/tarea-2")
def post_tarea_2(prenda:Tarea_2):
    return {"Respuesta": "Prenda agregada: Camisa"}