import json
from menu import *
from functions_client import *
from feature_travels import *
from aviones import *

saludo()
sub_saludo()

while True:
    limpiar()
    op=menu_principal()
    match op:
        case "1":
            menu_principal_clientes()
        case "2":
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
                        modificar_estado()
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

        case "3":
            print("Gracias por usar el sistema")
            break
        case _:
            print("Ingrese una opciòn valida")