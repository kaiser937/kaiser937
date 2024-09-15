from fastapi import FastAPI

app = FastAPI()

@app.get("/tarea-1")
def read_tarea():
    return {"respuesta": "Primer tarea realizada"}