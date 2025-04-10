import json
from menu import *
def leer_vuelos():
    with open ("vuelos.json","r") as file:
        vuelos=json.load(file)
    return vuelos


def escribir_vuelos(vuelos):
    with open ("vuelos.json","w") as file:
        json.dump(vuelos,file,indent=4)

def leer_aviones():
    with open ("aviones.json","r") as file:
        aviones=json.load(file)
    return aviones

def escribir_aviones(aviones):
    with open ("aviones.json","w") as file:
        json.dump(aviones,file,indent=4)

def crear_vuelo():
    vuelos=leer_vuelos()
    tickets=[]
    avion_existe=False
    aviones=leer_aviones()
    avion=input("Ingrese el avion: ")
    for avione in aviones:
        if avione["Codigo_avion"]==avion:
            avion_existe=True
            cantidad_asientos=avione["Asientos"]    

    if avion_existe==False:
        print("El avion no existe")
    
    else:
        vuelo_existe=False
        codigo=input("Ingrese el codigo: ")
        for vuelo in vuelos:   
            if vuelo["Codigo"]==codigo:
                vuelo_existe=True
                break    
        if vuelo_existe==True:
            print("El vuelo ya existe")
        else:
            origen=input("Ingrese el origen: ")
            destino=input("Ingrese el destino: ")
            fecha=input("Ingrese la fecha: ")
            while True:
                try:
                    precio=int(input("Ingrese el precio: "))
                    if precio>0:
                        break
                    else:
                        print("El precio no puede ser menor a 0")
                except ValueError:
                    print("El precio debe ser un numero")
            asiento=0
            for ticket in range(1,cantidad_asientos+1):
                codigo_ticket=codigo+str(ticket)
                tickets.append({"Ticket":codigo_ticket,
                "Precio":precio,
                "Asiento":asiento,
                "Vendido": False,
                "Cliente":""})
                asiento+=1
            vuelos.append({"Codigo":codigo,
                "Origen":origen,
                "Destino":destino,
                "Fecha":fecha,
                "Asientos":cantidad_asientos,
                "Tickets":tickets})
            escribir_vuelos(vuelos)
            tickets.clear()

def guardar_historial(vuelos, archivo="historial.txt"):
    with open(archivo, "a", encoding="utf-8") as f:
        for vuelo in vuelos:
            vendidos = [t for t in vuelo["Tickets"] if t["Vendido"]]
            if not vendidos:
                continue  # no guardar si no hay vendidos

            codigo = vuelo["Codigo"]
            origen = vuelo["Origen"]
            destino = vuelo["Destino"]
            fecha = vuelo["Fecha"]

            f.write(f"Viaje {codigo} ({origen} - {destino}) - Fecha: {fecha}\n")
            f.write("Tickets vendidos:\n")
            for ticket in vendidos:
                ticket_id = ticket["Ticket"]
                asiento = ticket["Asiento"]
                cliente = ticket["Cliente"]
                f.write(f"  Ticket: {ticket_id} | Asiento: {asiento} | Cliente: {cliente}\n")
            f.write("-" * 47 + "\n")

def iniciar_vuelo():
    vuelo_existe=False
    vuelos=leer_vuelos()
    codigo=input("Ingrese el codigo del vuelo: ")
    for vuelo in vuelos:   
        if vuelo["Codigo"]==codigo:
            vuelo_existe=True
            indice_vuelo=vuelos.index(vuelo)
    if vuelo_existe==True:
        vuelo = vuelos[indice_vuelo]
        guardar_historial([vuelo])
        vuelos.pop(indice_vuelo)
        escribir_vuelos(vuelos)
        print("El vuelo ha salido correctamente, se guardò en el historial")
    else: print("El vuelo no existe")

def gestion_vuelos_admin():
    while True:
        op=gestion_vuelos()
        limpiar()
        match op:
            case "1": 
                crear_vuelo()
                time.sleep(2)
                limpiar()
            case "2": 
                iniciar_vuelo()
                time.sleep(2)
                limpiar()
            case "3": 
                print( "Saliendo")
                time.sleep(1)
                limpiar() 
                break
            case _: print("Ingrese una opcion valida")

