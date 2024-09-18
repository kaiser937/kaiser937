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

@app.get("/tarea-3")
def get_tarea_3():
    return {"Reliquias": ["Calavera de cristal", "Arca de Noé"]}

class Tarea_3(BaseModel):
    Reliquia:str

@app.get("/tarea-3")
def post_tarea_3(Reliquia:Tarea_3):
    return {"Estado": "OK", "Reliquia": "Hojas de Tesla", "Actuales": ["Calavera de cristal", "Arca de Noé", "Hojas de Tesla"]}