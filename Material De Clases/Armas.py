"""
un jugador de video juegos desea comprar armas para su juego, espada 5.000, arco 7.000 y baston magico 9.000, el ususario puede comprar los articulos que el dese 
al oprimir la opcion salir el ususario debe ver su boleta, debe tener numero de identificacion, subtotal y total. 
"""
espada= 5000
arco= 7000
baston_m= 9000
descuento= 80


while True:
    def validar_nombre():
        while True:
            nombre=input("Ingrese su nombre: ")
            if len(nombre) >= 3:
                return nombre
            else:
                print("Error, el nombre debe tener almenos 3 caracteres")
#################################################################################
    def validar_rut():
        while True:
            rut= input("Ingrese su rut (sin putos ni guion): ")
            if len(rut) == 9:
                return rut
            else:
                print("Solo debe ingresar los 9 digitos de su rut")
##################################################################################
    def validar_descuento():
        while True:
            descuento_d=input("Deseas usar el codigo de 20% de descuento?(s/n): ").lower
            if descuento_d == "s":
                codigo=input("Ingrese el codigo de descuento: ")
                if codigo=="DUOCUC2026":
                    return descuento
                else:
                    print("Codigo invalido")
            else:
                break        
###################################################################################               
    print("=========Tienda de Armas=========")

    nombre= validar_nombre()
    rut= validar_rut()

    print("\nElije el arma que deseas comprar")
    while True:
        opcion=input("1.Espada\n2.Arco\n3.Baston Magico\n4.Salir\nElija una opcion: ")
        if opcion.isdigit() and len(opcion)>0:
            opcion=int(opcion)
            break
        else:
            print("Opcion invalida")
###################################################################################                
    if opcion == 1:
        total=espada
    elif opcion == 2:
        total=arco
    elif opcion == 3:
        total=baston_m
    else:
        print("Adios, hasta luego")
        break
###################################################################################
    descuento=validar_descuento()
    total_desc= (total*descuento)/100
###################################################################################    
    print("**********Boleta**********")
    print(f"\nNombre: {nombre}")
    print(f"\nRut: {rut}")
    print(f"\nMonto de la compra: ${total}")
    print(f"\nMonto a pagar: ${total_desc}")
    

