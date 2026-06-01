intento=5
while intento > 0:
    usuario=input("Ingrese su nombre de ususario: ")
    clave=int(input("Ingrese su clave: "))
    if usuario=="cristian" and clave==150303:
            print("Acceso correcto")
            print("*"*50)
            print(f"Bienvenido a su cunta de banco estado, {usuario}")
            print("*"*50)
            break
    else:
        intento-=1
        print("="*50)
        print(f"Datos incorrectos, Te quedan: {intento} intentos")
        print("="*50)
        if intento==0:
            print("Acceso Denegado")

      
