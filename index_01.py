intento = 3
while intento > 0:
    password=input("Dime tu clave: ")
    if password == "1234":
        print("Bienvenido")
        break
    else:
        intento -= 1
        
        print(f"Intento fallido, Te quedan, {intento}")
        if intento == 0:
            print("Acceso denegado")
            
"""
Usted ha sido seleccionado para realizar el nuevo sistema de login de banco estado el cual le permitira al usuario intentar un maximo de ingresos 
de 5 veces de no lograrlo debe mostrar el siguiente mensaje al usuario "Por favor comuniquese a nuestro Callcenter" de intrudicir correctamente su credencial
debe mostrar un mesaje de bienvenida con el nombre del usuario 
"""