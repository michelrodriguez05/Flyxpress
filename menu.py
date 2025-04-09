def menu_principal():
    menu_prin="""
    Menu Principal
    1.Clientes
    2.Empleados
    3.Salir"""
    print(menu_prin)
    return input("Ingrese una opciòn: ")

def menu_clientes():
    menuclientes="""
    Menu Clientes
    1.Iniciar sesion
    2.Registrarse
    3.Salir"""
    print(menu_clientes)
    return input ("Ingrese una opcion: ")

def cliente_sesion():
    cliente_sesion="""
    Cliente
    1.Comprar tickets
    2.Editar informacion
    3.Salir"""
    print(cliente_sesion)
    return input ("Ingrese una opciòn: ")

def cliente_tickets():
    cliente_tickets="""
    Vuelos
    1.Ver vuelos disponibles
    2.Comprar vuelos
    3.Salir
    """
    print(cliente_tickets)
    return input ("Ingrese una opciòn: ")

def menu_empleados():
    menu_empleados="""
    Empleados
    1.Gestion clientes
    2.Gestion vuelos
    3.Gestion aviones
    4.Salir"""
    print(menu_empleados)
    return input("Ingrese una opciòn: ")

def gestion_clientes():
    gescli="""
    Gestionar clientes
    1.Añadir
    2.Editar
    3.Eliminar
    4.Salir"""
    print(gescli)
    return input("Ingrese una opciòn: ")

def gestion_vuelos():
    gesvu="""
    Gestion vuelos
    1.Añadir vuelos
    2.Editar vuelos
    3.Salida vuelos
    4.Salir"""
    print(gesvu)
    return input("Ingrese una opciòn: ")

def gestion_aviones():
    gesavi="""
    Aviones
    1.Ver aviones disponibles
    2.Editar estado de aviones
    3.Salir"""
    print(gesavi)
    return input("Ingrese una opciòn: ")
