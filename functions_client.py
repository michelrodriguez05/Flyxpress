import json
import os
import time


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
        id_cliente = int(input("ID del cliente: "))
        if any(c["ID"] == id_cliente for c in clientes):
            print("El ID ya existe.")
            return
        nombre = input("Nombre del cliente: ")
        nuevo_cliente = {"ID": id_cliente, "Nombre": nombre, "Contraseña": None}
        clientes.append(nuevo_cliente)
        guardar_datos(clientes, ARCHIVO_CLIENTES)
        print("Cliente añadido. Ahora debe registrarse con una contraseña.")
    except ValueError:
        print("El ID debe ser un número entero.")
    except Exception as e:
        print(f"Error inesperado: {e}")

def registrar_o_iniciar_sesion():
    try:
        clientes = cargar_datos(ARCHIVO_CLIENTES)
        bloqueos = cargar_datos(ARCHIVO_BLOQUEOS)
        
        id_cliente = input("Ingrese su ID de cliente: ").strip()
        cliente = next((c for c in clientes if str(c["ID"]) == id_cliente), None)

        if not cliente:
            print("Cliente no encontrado.")
            return

        tiempo_bloqueo = bloqueos.get(id_cliente, 0)
        if tiempo_bloqueo > 0:
            print(f"Cliente bloqueado. Esperando {tiempo_bloqueo} segundos...")
            time.sleep(tiempo_bloqueo)

        if cliente["Contraseña"] is None:
            nueva_pass = input("Cree una contraseña: ")
            cliente["Contraseña"] = nueva_pass
            guardar_datos(clientes, ARCHIVO_CLIENTES)
            print("Registro exitoso.")
            return

        intentos = 3
        while intentos > 0:
            intento = input("Ingrese su contraseña: ")
            if intento == cliente["Contraseña"]:
                print(f"Bienvenido/a {cliente['Nombre']}.")
                bloqueos[id_cliente] = 0
                guardar_datos(bloqueos, ARCHIVO_BLOQUEOS)
                return
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
        id_buscar = int(input("ID del cliente a editar: "))
        cliente = next((c for c in clientes if c["ID"] == id_buscar), None)
        if not cliente:
            print("Cliente no encontrado.")
            return
        nuevo_nombre = input(f"Nuevo nombre (anterior: {cliente['Nombre']}): ")
        cliente["Nombre"] = nuevo_nombre
        guardar_datos(clientes, ARCHIVO_CLIENTES)
        print("Cliente editado.")
    except ValueError:
        print("El ID debe ser un número.")
    except Exception as e:
        print(f"Error al editar cliente: {e}")

def eliminar_cliente():
    try:
        clientes = cargar_datos(ARCHIVO_CLIENTES)
        id_eliminar = int(input("ID del cliente a eliminar: "))
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