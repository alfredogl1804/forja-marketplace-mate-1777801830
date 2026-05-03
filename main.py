from fastapi import FastAPI
from pydantic import BaseModel
import uuid

app = FastAPI(title="forja marketplace mate", version="1.0")

TUTORES = [
    {"id": 1, "nombre": "María González", "especialidad": "Álgebra", "precio_hora_mxn": 350},
    {"id": 2, "nombre": "Carlos Ramírez", "especialidad": "Cálculo", "precio_hora_mxn": 450},
    {"id": 3, "nombre": "Ana Martínez", "especialidad": "Geometría", "precio_hora_mxn": 380},
]

class ReservaRequest(BaseModel):
    tutor_id: int
    alumno_nombre: str
    fecha_iso: str

@app.get("/")
def root():
    return {"servicio": "forja marketplace mate", "version": "1.0"}

@app.get("/tutores")
def listar_tutores():
    return TUTORES

@app.post("/reservar")
def reservar(req: ReservaRequest):
    return {"reserva_id": str(uuid.uuid4()), "status": "confirmada"}
