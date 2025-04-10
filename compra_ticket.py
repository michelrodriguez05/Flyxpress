import json
def abrirArchivo(archivo):
    with open(f"{archivo}.json","r") as file:
        tiket=json.load(file)
    return tiket
def gusradraArchivo(archivo,diccionario):
    objetoJson=json.dumps(diccionario,indent=4)
    with open(f"{archivo}.json","w") as file:
        file.write(objetoJson)
    
def comprar_ticket():
    vuelo=abrirArchivo("vuelos")
    vuelo2=input("Ingrese el codigo del ticket ")
    existe=False
    for tickets in vuelo:
        for cod in tickets.items():
                for ticket in tickets:
                    for valor in tickets.items():
                        if cod==vuelo2: 
                            existe=True  
                               
    if existe==True:
        while True:
            opc=input("¿Desea comprar ese ticket(S/N):").upper()
            if opc=="S":
                for precio in tickets:
                    for valor in precio.items():
                        precio=valor["Precio"]
                        asiento=valor["Asiento"]
                cliente=input("Ingrese el codigo del cliente:")
                vuelos={
                    "Ticket":vuelo2,
                    "Precio":precio,
                    "Asiento":asiento,
                    "Vendido":True,
                    "Cliente":cliente
                }
                vuelo.append(vuelos)
                gusradraArchivo("vuelos",vuelo)
                break
            
comprar_ticket()