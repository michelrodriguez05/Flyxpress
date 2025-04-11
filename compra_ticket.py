import json
def abrirArchivo(archivo):
    with open(f"{archivo}.json","r") as file:
        tiket=json.load(file)
    return tiket
def gusradraArchivo(archivo,diccionario):
    objetoJson=json.dumps(diccionario,indent=4)
    with open(f"{archivo}.json","w") as file:
        file.write(objetoJson)
    
def comprar_ticket(id_cliente):
    vuelos=abrirArchivo("vuelos")
    clientes=abrirArchivo("clientes")
    cod_ticket=input("Ingrese el codigo del ticket:")
    existe=False
    for vuelo in vuelos:
        if vuelo["Tickets"]:
                for ticket in vuelo["Tickets"]:
                    if ticket.get("Ticket")==cod_ticket:
                        if ticket["Vendido"]: 
                            pass
                        else:
                            ticket["Vendido"] = True
                            ticket["Cliente"] = id_cliente
                            print("¡Ticket comprado exitosamente!")
                            gusradraArchivo("vuelos",vuelos)
                            for cliente in clientes:
                                if cliente["ID"]==id_cliente:
                                    cliente["Tickets"].append({"Codigo":cod_ticket})
                                    gusradraArchivo("clientes",clientes)
                                    print("Se comprò el ticket correctamente")

                        existe = True
                        break
        if existe:
            break 

    if not existe:
        print("El código de ticket ingresado no existe.")
                          
def mostrar_tickets_cliente():
    tickets=abrirArchivo("vuelos")
    clientes=abrirArchivo("clientes")
    id=input("Ingrese el ID del cliente: ")
    for cliente in clientes:
        if cliente["ID"]==id:
            print("---------------------------------")
            print(f"              {id}              ")
            for clave,valor in cliente.items():
                if clave=="Tickets":
                    for valore in valor:
                        for clave1,valor1 in valore.items():
                            print(f"{clave1}->{valor1}")
            print("---------------------------------")
            
            
            
