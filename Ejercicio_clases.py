
"""
Tienes tu primer empleo en el ritei falabella y necesitan realizar un programa el python, que entrege descuento a los clientes y para 
ello comenzamo pidiendole al usuario su rut, el cual debe validar los ocho digitos del mismo en una casilla posterior validar el codigo de verificacion del rut 
posterirmente se le pide el nombre, monto de la compra para saber si obtiene el descuento si o no toda compra menor a 10mil pesos no obtiene descuento 
toda compra mayor a 11mil peso hasta 50mil pesos obtiene un 10% de descuento y toda compra mayor a 50mil pesos obtiene un 20% de descuento
que deberia calcular mi programa: monto de descuento, total a pagar y debe mostrar en pantalla tipo boleta el nuemro de identificacion del usuario, nombre
monto de la compra, descuento aplicado y total de la compra 
"""
while True:
    nombre=input("ingrese su nombre: ")
    rut=int(input("Ingrese los primeros 8 digitos de su rut: "))
    digito_verificador=int(input("Ingrese su digito verificador: "))

    if rut == 21267665 and digito_verificador == 9:
        print("Bienvenido a tu tienda Falabella online")
        monto=int(input("Por favor ingrese el monto de su compra: "))
        if monto < 10000:
            print("Gracias por comprar con nosotros..")
            print("*"*55)
            print("               Boleta de compra online")
            print()
            print(f"Nombre del cliente: {nombre}")
            print(f"Numero de indentificacion: {rut}-{digito_verificador}")
            print(f"Monto a pagar: $ {monto}")
            print("No aplica descuento")
            print()
            print("*"*55)
            break
        elif monto > 10000 and monto < 50000:
                monto_final= monto*0.10
                print("Gracias por comprar con nosotros..")
                print("*"*55)
                print("               Boleta de compra online")
                print()
                print(f"Nombre del cliente: {nombre}")
                print(f"Numero de indentificacion: {rut}-{digito_verificador}")
                print(f"Monto de la compra: $ {monto}")
                print("Descuento aplicado de un 10%")
                print(f"Su monto total a pagar es: $ {(monto-monto_final)}")
                print("*"*55)
                break
        else:
              print("Gracias por comprar con nosotros..")
              print("*"*55)
              print("               Boleta de compra online")
              print()
              print(f"Nombre del cliente: {nombre}")
              print(f"Numero de indentificacion: {rut}-{digito_verificador}")
              print(f"Monto de la compra: $ {monto}")
              print("Descuento aplicado de un 20%")
              print(f"Su monto total a pagar es: $ {(monto*0.80)}")
              print("*"*55)
              break   
    else:
         print("Datos incorrectos, intente de nuevo")          