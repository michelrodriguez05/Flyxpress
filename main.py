import json
from menu import *
from functions_client import *
from feature_travels import *
from aviones import *

# saludo()
# sub_saludo()
contra="holamundo"
while True:
    limpiar()
    op=menu_principal()
    match op:
        case "1":
            menu_principal_clientes()
        case "2":
            limpiar()
            clave=input("Ingrese la clave: ")
            if clave==contra:
                print("Clave correcta")
                time.sleep(1)
                limpiar()
                while True:
                    op=menu_empleados()
                    limpiar()
                    match op:
                        case "1": 
                            gestion_clientes_admin()
                            time.sleep(1)
                            limpiar()
                        case "2": 
                            gestion_vuelos_admin()
                            time.sleep(1)
                            limpiar()
                        case "3": 
                            gestionaviones()
                            time.sleep(1)
                            limpiar()
                        case "4": 
                            print("Saliendo")
                            time.sleep(1)
                            limpiar()
                            break
                        case _: 
                            print("Ingresa una opcion valida")
                            time.sleep(1)
            else:
                print("Contraseña incorrecta")
                time.sleep(2)

        case "3":
            print("Gracias por usar el sistema")
            break
        case _:
            print("Ingrese una opciòn valida")