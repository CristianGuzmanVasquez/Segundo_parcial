# Sistema de vehiculos

def mostrar_menu():

    print("")
    print("_"*7+"Menu principal"+"_"*7)
    print("1.- Agregar vehiculo")
    print("2.- Buscar vehiculo")
    print("3.- Eliminar vehiculo")
    print("4.- Actualizar vehiculo")
    print("5.- Mostrar vehiculos")
    print("6.- Salir")
    print("_"*28)

# Funcion para leer 

def leer_opcion():

    try:
        opcion=int(input("Selecciona una opcion: "))
        if 1 <= opcion <= 6:
            return opcion
        else:
            print("Error, ingrese una opcion del 1 al 6")
            return 0
    except ValueError:
        print("Ingresa un numero entero")

# Funcion modelo        
            
def validacion_modelo(modelo):

    if modelo.strip() != "":
        return True
    else:
        return False
    
# Funcion año     

def validar_anio(anio):

    if anio > 1900:
        return True
    else:
        return False
    
# Funcion de precio

def validar_precio(precio):

    if precio > 0:
        return True
    else:
        return False

# Funcion de vehiculo

def agregar_vehiculo(lista_vehiculos):

    print()        
    print("Agregar vehiculo")

    modelo = input("Agrega el model del vehiculo: ")
    if not validacion_modelo(modelo):
        print("Error, el modelo no puede estar vacio.")
        return
    
    try:
        anio = int(input("Ingresa el año del vehiculo: "))
        if not validar_anio(anio):
            print("Error, el año debe ser mayor que 1900.")
            return
    except ValueError:
        print("Error, Debe ingresar un año valido")
        return

    try:
        precio = float(input("Ingrese el precio del vehiculo: "))
        if not validar_precio(precio):
            print("Error, el precio debe ser mayor que cero")
            return
    except ValueError:
        print("Error, el precio debe ser un numero decimal")
        return

    vehiculo = {
        "modelo": modelo.strip(),
        "anio": anio,
        "precio": precio,
        "disponible": False
    }    

    lista_vehiculos.append(vehiculo)

    print("Vehiculo agregado correctamente.")
    
# Funcion buscar vehiculo

def buscar_vehiculo(lista_vehiculos, modelo_buscado):
    modelo_buscado = modelo_buscado.strip().lower
    
    for i in range(len(lista_vehiculos)):
        modelo_actual = lista_vehiculos[i]["modelo"].strip().lower()
        if modelo_actual == modelo_buscado:
            return i
    return -1

# Funcion mostrar vehiculo

def mostrar_datos_vehiculo(vehiculo):
    print("Modelo:", vehiculo["modelo"])
    print("Año:", vehiculo["anio"])
    print("Precio:", vehiculo["precio"])  

    if vehiculo["disponible"] == True:
        print("Estado: DISPONIBLE")
    else:
        print("Estado: NO DISPONIBLE")    

# Funcion eliminar vehiculo

def eliminar_vehiculo(lista_vehiculos):
    print()
    print("=== ELIMINAR VEHICULO ===")
    
    modelo=input("Ingrese el modelo del vehiculo que desea eliminar: ")
    posicion=buscar_vehiculo(lista_vehiculos,modelo)
    
    if posicion != -1:
        lista_vehiculos.pop(posicion)
        print("Vehiculo eliminado correctamente.")
    else:
        print(f"El vehiculo '{modelo}' no se encuentra registrado.")
        
# Funcion actualizar vehiculos

def actualizar_disponibilidad(lista_vehiculos):
    for vehiculo in lista_vehiculos:
        if vehiculo ["anio"] >= 2020:
            vehiculo["disponible"]=True
        else:
            vehiculo["disponible"]=False        

# Funcion mostrar vehiculo

def mostrar_vehiculos(lista_vehiculos):
    print()
    print("=== LISTA DE VEHICULOS ===")
    
    actualizar_disponibilidad(lista_vehiculos)
    
    if len(lista_vehiculos)==0:
        print("No hay vehiculos registrados.")
        return
    
    for vehiculo in lista_vehiculos:
        mostrar_datos_vehiculo(vehiculo)
        print("*"*45)
            
#  PROGRAMA PRINCIPAL

vehiculos = []

while True:
    mostrar_menu()
    opcion=leer_opcion()
    
    if opcion == 1:
        agregar_vehiculo(vehiculos)
    elif opcion == 2:
        print()
        print("=== BUSCAR VEHICULO ===")
        
        modelo=input("Ingrese el modelo del vehiculo a buscar: ")
        posicion =buscar_vehiculo(vehiculos,modelo)
        
        if posicion != -1:
            print("Vehiculo encontrado en la posicion:", posicion)
            actualizar_disponibilidad(vehiculos)
            mostrar_datos_vehiculo(vehiculos[posicion])
        else:
            print("Vehiculo no encontrado.")
    elif opcion == 3:
        eliminar_vehiculo(vehiculos)
    elif opcion == 4:
        actualizar_disponibilidad(vehiculos)
        print("Disponibilidad actualizada correctamente.")
    elif opcion == 5:
        mostrar_vehiculos(vehiculos)
    elif opcion == 6:
        print("Gracias por usar el sistema. Vuelva pronto")
    else:
        print("Intente nuevamente.")                                




