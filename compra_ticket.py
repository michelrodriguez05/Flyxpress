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
    for vuelo in vuelo:
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
                          
    
            
