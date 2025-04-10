import json
from manejador_json import cargar_datos, guardar_datos

FILE_AVIONES = "vuelos.json"

def listar_tickets():
    vuelos = cargar_datos(FILE_AVIONES)

    if not vuelos:
        print("No hay vuelos disponibles")
        return

    
    vuelos_no_vendidos = []
    for vuelo in vuelos:
        for ticket in vuelo.get("Tickets", []): 
            if not ticket["Vendido"]:
                vuelos_no_vendidos.append((vuelo, ticket))  

    if vuelos_no_vendidos:
        print("\n--- Lista de vuelos disponibles ---")
        for vuelo, ticket in vuelos_no_vendidos:
            print(f"\nCódigo: {vuelo['Codigo']}")
            print(f"Origen: {vuelo['Origen']}")
            print(f"Destino: {vuelo['Destino']}")
            print(f"Fecha: {vuelo['Fecha']}")
            print(f"Ticket: {ticket['Ticket']}")
            print(f"Precio: ${ticket['Precio']}")
            print(f"Asiento: {ticket['Asiento']}")
            print(f"Vendido: {'Sí' if ticket['Vendido'] else 'No'}")
            print(f"Cliente: {ticket['Cliente'] if ticket['Cliente'] else 'N/A'}")
            print("-------------------------")  
    else:
        print("No hay vuelos disponibles")
