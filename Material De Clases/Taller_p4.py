
productos=[]

def mostrar_menu():
    print("=======MENU PRINCIPAL=======")
    print("1. Agregar producto")
    print("2. Buscar producto")
    print("3. Eliminar producto")
    print("4. Actualizar disponibilidad")
    print("5. Mostrar producto")
    print("6. Salir")
    print("="*28)

def leer_opcion():
    try:
        opcion=int(input("Seleccione una opcion: "))
        if 1<= opcion <= 6:
            return opcion
        else:
            print("Error, Ingrese un numero del 1 al 6.")
            return 0
    except ValueError:
        print("Error, Ingrese un numero entero.")
        return 0
        
def nombre_producto(nombre):
    if nombre.strip() !="":
        return True
    else:
        return False
    
def stock_producto(stock):
    if stock >= 0:
        return True
    else:
        return False
    
def precio_producto(precio):
    if precio > 0:
        return True
    else:
        return False

def agregar_producto(lista_productos):
    print()
    print("=====AGREGAR PRODUCTO=====")
    nombre=input("Nombre del producto: ")
    if not nombre_producto(nombre):
        print("Error, El nombre no puede estar vacio.")
        return
    
    try:
        stock=int(input("Stock del producto: "))
        if not stock_producto(stock):
            print("Error, El stock debe ser mayor a cero.")
            return
    except ValueError:
        print("Error, Ingrese solo numeros enteros positivos.")
        return

    try:
        precio=float(input("Precio del producto: "))
        if not precio_producto(precio):
            print("Error, Ingrese un numero decimal mayor a cero.")
            return
    except ValueError:
        print("Error, Ingrese solo numeros decimales.") 
        return

    producto={
        "nombre" : nombre.strip(),
        "stock"  : stock,
        "precio" : precio,
        "disponible" : False
    }       
    lista_productos.append(producto)
    print("Producto agregado con exito!")

def buscar_producto(lista_productos, nombre_buscado):
    nombre_buscado=nombre_buscado.strip().lower()
    for i in range(len(lista_productos)):
        nombre_actual=lista_productos[i]["nombre"].strip().lower()
        if nombre_actual==nombre_buscado:
            return i
    return -1
    
def mostrar_datos_producto(producto):
    print("Nombre:",producto["nombre"])
    print("Stock:",producto["stock"])
    print("Precio:",producto["precio"])
    if producto["disponible"]==True:
        print("Estado: DISPONIBLE")
    else:
        print("Estado: SIN STOCK")    

def eliminar_producto(lista_productos):
    print()
    print("=====ELIMINAR PRODUCTO=====")
    nombre=input("Nombre del producto que desea eliminar: ")
    posicion=buscar_producto(lista_productos, nombre)
    if posicion != -1:
        lista_productos.pop(posicion)
        print("Producto eliminado con exito.")
    else:
        print(f"El producto '{nombre}' no se encuentra registrado.")

def actualizar_disponibilidad(lista_productos):
    for producto in lista_productos:
        if producto["stock"] > 0:
            producto["disponible"]= True
        else:
            producto["disponible"]= False

def mostrar_producto(lista_productos):
    actualizar_disponibilidad(lista_productos)
    print()
    if len(lista_productos)== 0:
        print("No existen productos registrados.")
        return
    
    for producto in lista_productos:
        mostrar_datos_producto(producto)
        print("*"*47)

while True:
    mostrar_menu()
    opcion=leer_opcion()
    if opcion == 1:
        agregar_producto(productos)
    elif opcion == 2:
        print("\n=====BUSCAR PRODUCTO=====")
        nombre=input("Ingrese el nombre del producto que desea buscar: ")
        posicion=buscar_producto(productos,nombre)
        if posicion != -1:
            print(f"Producto encontrado en la posicion {posicion}")
            actualizar_disponibilidad(productos)
            mostrar_datos_producto(productos[posicion])
        else:
            print("Producto no encontrado.")
    elif opcion == 3:
        eliminar_producto(productos)
    elif opcion == 4:
        actualizar_disponibilidad(productos)
        print("Disponibilidad actualizada.")
    elif opcion ==5:
        mostrar_producto(productos)
    elif opcion == 6:
        print("Gracias por usar el sistema. Vuelva Pronto")
        break
    else:
        print("Ingrese una opcion valida.")                                    






