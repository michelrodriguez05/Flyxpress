import json
import os
import time
from menu import *
from compra_ticket import *
from lista_tickets import *

ARCHIVO_CLIENTES = "clientes.json"
ARCHIVO_BLOQUEOS = "bloqueos.json"

# --------------------- UTILIDADES ---------------------

def cargar_datos(archivo):
    try:
        if not os.path.exists(archivo):
            return [] if archivo == ARCHIVO_CLIENTES else {}
        with open(archivo, "r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, IOError) as e:
        print(f"Error al cargar '{archivo}': {e}")
        return [] if archivo == ARCHIVO_CLIENTES else {}

def guardar_datos(data, archivo):
    try:
        with open(archivo, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
    except IOError as e:
        print(f"Error al guardar en '{archivo}': {e}")

# --------------------- FUNCIONES PRINCIPALES ---------------------

def añadir_cliente():
    try:
        clientes = cargar_datos(ARCHIVO_CLIENTES)
        id_cliente = (input("ID del cliente: "))
        if any(c["ID"] == id_cliente for c in clientes):
            print("El ID ya existe.")
            return
        nombre = input("Nombre del cliente: ")
        while True:
            contraseña=input("Ingrese una contraseña: ")
            contraseña2=input("Confirme la contraseña: ")
            if contraseña==contraseña2:
                print("Las contraseñas coinciden")
                break
            else: print("Las contraseñas no coinciden")
        nuevo_cliente = {"ID": id_cliente, "Nombre": nombre, "Contrasenia": contraseña, "Tickets":[]}
        clientes.append(nuevo_cliente)
        guardar_datos(clientes, ARCHIVO_CLIENTES)
        print("Cliente añadido con exito")
    except ValueError:
        print("El ID debe ser un número entero.")
    except Exception as e:
        print(f"Error inesperado: {e}")

def iniciar_sesion():
    acceso=False
    try:
        clientes = cargar_datos(ARCHIVO_CLIENTES)
        bloqueos = cargar_datos(ARCHIVO_BLOQUEOS)
        
        id_cliente = input("Ingrese su ID de cliente: ")
        cliente = next((c for c in clientes if str(c["ID"]) == id_cliente), None)

        if not cliente:
            print("Cliente no encontrado.")
            return id_cliente, acceso
        

        tiempo_bloqueo = bloqueos.get(id_cliente, 0)
        if tiempo_bloqueo > 0:
            print(f"Cliente bloqueado. Esperando {tiempo_bloqueo} segundos...")
            time.sleep(tiempo_bloqueo)

        intentos = 3
        while intentos > 0:
            intento = input("Ingrese su contraseña: ")
            if intento == cliente["Contrasenia"]:
                print(f"Bienvenido/a {cliente['Nombre']}.")
                bloqueos[id_cliente] = 0
                guardar_datos(bloqueos, ARCHIVO_BLOQUEOS)
                acceso=True
                return id_cliente, acceso
            else:
                intentos -= 1
                print(f"Contraseña incorrecta. Intentos restantes: {intentos}")

        nuevo_bloqueo = bloqueos.get(id_cliente, 0) + 5
        bloqueos[id_cliente] = nuevo_bloqueo
        guardar_datos(bloqueos, ARCHIVO_BLOQUEOS)
        print(f"Demasiados intentos. Bloqueado por {nuevo_bloqueo} segundos.")
        
    except Exception as e:
        print(f"Error en inicio de sesión: {e}")

def editar_cliente():
    try:
        clientes = cargar_datos(ARCHIVO_CLIENTES)
        id_buscar = (input("ID del cliente a editar: "))
        cliente = next((c for c in clientes if c["ID"] == id_buscar), None)
        if not cliente:
            print("Cliente no encontrado.")
            return
        nuevo_nombre = input(f"Nuevo nombre (anterior: {cliente['Nombre']}): ")
        cliente["Nombre"] = nuevo_nombre
        cliente["Contrasenia"]=input("Ingresa una contraseña nueva: ")
        guardar_datos(clientes, ARCHIVO_CLIENTES)
        print("Cliente editado.")
    except ValueError:
        print("El ID debe ser un número.")
    except Exception as e:
        print(f"Error al editar cliente: {e}")


def editar_cliente_cliente(id_cliente):
    try:
        clientes = cargar_datos(ARCHIVO_CLIENTES)
        cliente = next((c for c in clientes if c["ID"] == id_cliente), None)
        if not cliente:
            print("Cliente no encontrado.")
            return
        nuevo_nombre = input(f"Nuevo nombre (anterior: {cliente['Nombre']}): ")
        cliente["Nombre"] = nuevo_nombre
        cliente["Contrasenia"]=input("Ingresa una contraseña nueva: ")
        guardar_datos(clientes, ARCHIVO_CLIENTES)
        print("Cliente editado.")
    except ValueError:
        print("El ID debe ser un número.")
    except Exception as e:
        print(f"Error al editar cliente: {e}")

def eliminar_cliente():
    try:
        clientes = cargar_datos(ARCHIVO_CLIENTES)
        id_eliminar = (input("ID del cliente a eliminar: "))
        nuevos_clientes = [c for c in clientes if c["ID"] != id_eliminar]
        if len(nuevos_clientes) == len(clientes):
            print("Cliente no encontrado.")
        else:
            guardar_datos(nuevos_clientes, ARCHIVO_CLIENTES)
            print("Cliente eliminado.")
    except ValueError:
        print("El ID debe ser numérico.")
    except Exception as e:
        print(f"Error al eliminar cliente: {e}")

def menu_principal_clientes():
    limpiar()
    while True:
        op=menu_clientes()
        limpiar()
        match op:
            case "1": 
                id_cliente, acceso=iniciar_sesion()
                time.sleep(1)
                limpiar()
                if acceso==True:
                    while True:
                        op=cliente_sesion()
                        time.sleep(1)
                        limpiar()
                        match op:
                            case "1": 
                                while True:
                                    op=cliente_tickets()   
                                    time.sleep(1)
                                    limpiar()
                                    match op:
                                        case "1":
                                            limpiar()
                                            listar_tickets()
                                            input("Ingrese cualquier tecla para volver")
                                            limpiar()
                                        case "2":
                                            comprar_ticket(id_cliente)
                                            time.sleep(1)
                                            limpiar()
                                        case "3":    
                                            print("Saliendo")
                                            time.sleep(1)
                                            limpiar()
                                            break
                                        case _: 
                                            print("Ingresa una opcion valida")
                                            time.sleep(1)
                            case "2": 
                                editar_cliente_cliente(id_cliente)
                                time.sleep(1)
                                limpiar()
                            case "3": 
                                mostrar_tickets_cliente()
                                input("Ingrese cualquier tecla para volver")
                                limpiar()
                            case "4":
                                print("Saliendo")
                                time.sleep(1)
                                limpiar()
                                break
                            case _: 
                                print("Ingrese una opcion valida")
                                time.sleep(1)
            case "2": 
                añadir_cliente()
                time.sleep(1)
                limpiar()
            case "3":
                print("Saliendo")
                time.sleep(1)
                limpiar()
                break

def consulta_clientes():
    with open("clientes.json","r") as file:
        clientes=json.load(file)
    existe=False
    id=input("Ingrese el id del cliente: ")
    for cliente in clientes:
        if cliente["ID"]==id:
            existe=True
            for clave, valor in cliente.items():
                print(f"{clave}->{valor}")
    if existe==False: print("CLiente no existe")

def gestion_clientes_admin():
    while True:
        limpiar()
        op=gestion_clientes()
        match op:
            case "1": 
                añadir_cliente()
                time.sleep(1)
            case "2": 
                editar_cliente()
                time.sleep(1)
            case "3": 
                eliminar_cliente()
                time.sleep(1)
            case "4": 
                consulta_clientes()
                input("Ingrese cualquier tecla para continuar: ")
                limpiar()
            case "5":
                print("Saliendo")
                time.sleep(1)
                limpiar()
                break
            case _: 
                print("Ingresa una opcion valida")
                time.sleep(1)
                
