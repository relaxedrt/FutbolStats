# Para Ejecutar La Api Hay Que Usar El Comando "fastapi dev ./API/api.py
from fastapi import FastAPI, Response
import json

app = FastAPI()

@app.get("/")
async def root():
    # Establecemos La Ruta Del JSON Que Vamos A Leer
    filepath = './Datos/ranking.json'

    # Abrimos El Archivo JSON En Modo Lectura
    with open(filepath, "r") as dataFile:
        # Leemos El Contenido Del Archivo Y Lo Cargamos Como Un Objeto JSON En La Variable data
        data = json.load(dataFile)
        
        # Convertimos El Objeto JSON De Vuelta A Una Cadena Con Formato JSON Y Lo Identamos Para Mejorar Su legibilidad
        pretty_json = json.dumps(data, indent=4)
        
    # Retornamos La Respuesta Usando Response De FastAPI Y Usamos media_type="application/json" Para Que Lo Reconozca Como JSON
    return Response(content=pretty_json, media_type="application/json")