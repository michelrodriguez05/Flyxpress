import json

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
