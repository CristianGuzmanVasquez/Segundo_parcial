
def mostrar_menu():
    print("")
    print("="*7+"MENU PRINCIPAL"+"="*7)
    print("1.- Agregar paciente")
    print("2.- Buscar paciente")
    print("3.- Eliminar paciente")
    print("4.- Actualizar estado")
    print("5.- Mostrar pacientes")
    print("6.- Salir")
    print("="*28)

def leer_opcion():
    opcion=int(input("Seleccione una opcion: "))
    try:
        if 1 <= opcion <= 6:
            return opcion
        else:
            print("Ingrese una opcion valida")
    except ValueError:
        print("Ingrese un numero del 1 al 6")

def validacion_nombre(nombre):
    if nombre.strip() != "":
        return True
    else:
        return False
     
def validacion_edad(edad):
    if edad > 0:
        return True
    else:
        return False

def validacion_temperatura(temperatura):
    if 35.0 <= temperatura <= 42.0:
        return True
    else:
        return False
    
def agregar_paciente(lista_pacientes):
    print()
    print("Agregar paciente")
    nombre=input("Ingrese el nombre del paciente: ")
    if not validacion_nombre(nombre):
        print("Error, El nombre no puede estar vacio")
        return
    
    try:
        edad=int(input("Ingrese la edad del paciente: "))
        if not validacion_edad(edad):
            print("Error, Ingrese una edad mayor que cero.")
            return
    except ValueError:
        print("Error, Ingrese un numero entero mayor que cero.")
        return

    try:
        temperatura=float(input("Ingrese la temperatura del paciente: "))
        if not validacion_temperatura(temperatura):
            print("Error, La temperatura debe ser un decimal entre 35.0 y 42.0 .")
            return
    except ValueError:
        print("Error, Ingrese un numero decimal.")
        return

    paciente={
        "nombre":nombre.strip(),
        "edad":edad,
        "temperatura":temperatura,
        "estado": False
    }                
    lista_pacientes.append(paciente)
    print("Paciente agregado con exito.")

def buscar_paciente(lista_pacientes,nombre_buscado):
    nombre_buscado=nombre_buscado.strip().lower()

    for i in range(len(lista_pacientes)):
        nombre_actual=lista_pacientes[i]["nombre"].strip().lower()
        if nombre_actual==nombre_buscado:
            return i
    return -1

def mostrar_datos_paciente(paciente):
    print("Nombre:", paciente["nombre"])
    print("Edad:", paciente["edad"])
    print("Temperatura:", paciente["temperatura"])

    if paciente["estado"]==True:
        print("Estado: ATENDIDO")
    else:
        print("Estado: REQUIERE ATENCION")  

def eliminar_paciente(lista_pacientes):
    print()
    print("====ELIMINAR PACIENTE====")

    nombre=input("Ingrese el nombre del paciente que desea eliminar: ")
    posicion=buscar_paciente(lista_pacientes,nombre)
    if posicion != -1:
        lista_pacientes.pop(posicion)
        print("Paciente eliminado con exito.")
    else:
        print(f"El paciente '{nombre}' no se encuentra registrado.")

def actualizar_estado(lista_pacientes):
    for paciente in lista_pacientes:
        if paciente["temperatura"] <= 37.0:
            paciente["estado"]=True
        else:
            paciente["estado"]=False

def mostrar_pacientes(lista_pacientes):
    print()
    print("====LISTA PACIENTES====")
    actualizar_estado(lista_pacientes)

    if len(lista_pacientes)==0:
        print("No hay pacientes registrados.")
        return
    
    for paciente in lista_pacientes:
        mostrar_datos_paciente(paciente)
        print("*"*45)

pacientes=[]

while True:
    mostrar_menu()
    opcion=leer_opcion()

    if opcion == 1:
        agregar_paciente(pacientes)
    elif opcion == 2:
        print()
        print("==== BUSCAR PACIENTE ====")

        nombre=input("Ingrese el nombre del paciente a buscar: ")
        psicion=buscar_paciente(pacientes,nombre)

        if psicion != -1:
            print("Paciente encontrado")
            actualizar_estado(pacientes)
            mostrar_datos_paciente(pacientes[psicion])
        else:
            print("Paciente no encontrado.")
    elif opcion == 3:
        eliminar_paciente(pacientes)
    elif opcion == 4:
        actualizar_estado(pacientes)
        print("Estados actualizados correctamente.")
    elif opcion == 5:
        mostrar_datos_paciente(pacientes)
    elif opcion == 6:
        print("Gracias por usar el sistema, Vuelva Pronto")
        break
    else:
        print("Intente nuevamente.")                               