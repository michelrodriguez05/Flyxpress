from manejador_json import cargar_datos, guardar_datos
import json, time, os
from menu import gestion_aviones, limpiar
FILE_AVIONES = "aviones.json"


def modificar_estado():
        aviones = cargar_datos(FILE_AVIONES)
        codigo = input("Ingrese el codigo del avion: ")

        avion_encontrado = False  

        for p in aviones:
            if p["Codigo_avion"]== codigo:
                avion_encontrado = True

        if avion_encontrado==True:  
                while True:  
                    nuevo_estado = input("Ingresa 'activo' o 'inactivo': ").strip().lower()
                    if nuevo_estado == "activo":
                        p["estado"] = True
                        print("Estado actualizado a activo.")
                        guardar_datos(FILE_AVIONES, aviones)
                        break
                    elif nuevo_estado == "inactivo":
                        p["estado"] = False
                        print("Estado actualizado a inactivo")
                        guardar_datos(FILE_AVIONES, aviones)
                        break
                    else:
                        print("Escribe una opcion correcta")

        elif not avion_encontrado:
                print("Avion con el codigo proporcionado no encontrado")

def mostrar_aviones():
    with open("aviones.json","r")as file:
        aviones=json.load(file)
    for avion in aviones:
        print("--------------------------")
        for clave, valor in avion.items():
            print(f"{clave}->{valor}")
        print("--------------------------")
        

def gestionaviones():
    while True:
        op=gestion_aviones()
        match op:
            case "1":
                  mostrar_aviones()
                  input("Ingrese cualquier tecla para volver: ")
                  limpiar()
            case "2":
                  modificar_estado()
                  time.sleep(2)
                  limpiar()
            case "3":
                print("Saliendo")
                time.sleep(1)
                limpiar()
                break
            case _:print("Ingrese una opcion valida")
    