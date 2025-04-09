import json
import os

def cargar_datos(archivo):
    
    if not os.path.exists(archivo):
        guardar_datos(archivo, [])  
        return []

    try:
        with open(archivo, "r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, FileNotFoundError):
        return []  

def guardar_datos(archivo, datos):
   
    with open(archivo, "w", encoding="utf-8") as file:
        json.dump(datos, file, indent=4, ensure_ascii=False)
        