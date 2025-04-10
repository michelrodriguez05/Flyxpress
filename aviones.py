from manejador_json import cargar_datos, guardar_datos
import json

FILE_AVIONES = "aviones.json"


def modificar_estado():
        aviones = cargar_datos(FILE_AVIONES)
        codigo = input("Ingrese el codigo del avion: ").strip().lower()

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



