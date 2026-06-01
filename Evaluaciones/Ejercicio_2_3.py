cupo_maximo=75
cupo_libre=75
cupo_ocupado=0
print ("¡Bienvenido al sistema de gestión de cupos del Gimnasio Titan!")
while True:
   
    print("*"*15+"MENU PRINCIPAL"+"*"*15)
    print("\n1.Cupos disponibles.\n2.Realizar reserva.")
    print("3.Cancelar reserva.\n4.Historial de reservas.")
    print("5.Salir")
    try:
        opcion=int(input("Ingrese una opcion: "))
    except ValueError:
        print("Opcion invalida, ingrese un numero")
        continue
    if opcion==1:
        print(f"Los cupos disponibles son: {cupo_libre} ")
    elif opcion==2:
        while True:
            try:
                cantidad=int(input("Ingrese los cupos que desea matricular: "))
                if cantidad>0:
                    break
                else:
                    print("Debe ingresar un numero positivo.")
            except ValueError:
                print("Error!!, ingrese un numero entero positivo.")
        if cantidad>cupo_libre:
            print("No tenemos espacios disponibles")
        else:
            cupo_libre-=cantidad
            cupo_ocupado+=cantidad
            print("Reserva realizada con exito!!")
    elif opcion==3:
        while True:
            try:
                cantidad=int(input("Ingrese la cantidad de cupos que desea cancelar: "))
                if cantidad>0:
                    break
                else:
                    print("Error!!,Ingrese un numero positivo")
            except ValueError:
                print("Ingrese solo numeros positivos")
        if cantidad > cupo_ocupado:
            print("No se pueden liberar mas cupos de los ya usados")
        elif (cupo_libre+cantidad)>cupo_maximo:
            print(f"Supero la capacidad maxima de cupos {cupo_maximo}")
        else:
            cupo_libre+=cantidad
            cupo_ocupado-=cantidad
            print("Reserva cancelada con exito!!")
    elif opcion==4:
        print(f"Reservas registradas: {cupo_ocupado}\nReservas Libres: {cupo_libre}")
    elif opcion==5:
        print("Gracias por utilizar nuestro software, hasta la próxima")
        break
    else:
        print("Opcion invalida!")                                                                       