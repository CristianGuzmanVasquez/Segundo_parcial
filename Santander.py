"""
Estimado estudiante usted ha sido seleccionado para realizar la interfaz de usuario de los cajeros automaticos del grupo santander 
el programa debe solicitar al usuario numero de rut, el cual debe ser validado con su numero de verificacion posteriormente 
el ususario debe introducir su clave que no debe ser mayor o menor a diez digitos. ¡Suerte!

"""
def validar_rut(rut):
    rut = rut.replace(".", "").replace("-", "").upper()
    cuerpo, dv = rut[:-1], rut[-1]                    
    suma = sum(int(d)*f for d, f in zip(reversed(cuerpo), [2,3,4,5,6,7]*10))
    res = 11 - (suma % 11)                              
    dv_calc = "0" if res == 11 else "K" if res == 10 else str(res)
    return dv == dv_calc
while True:
    print("-"*55)
    print("                Banco Santander")
    print()
    print("-Por favor ingrese sus datos ")
    print()
    rut=input("Ingrese su rut,(con puntos y guion): ")
    if (validar_rut(rut)):
        clave=input("ingrese su clave: ")
        if len(clave) >10 or len(clave)<10: 
            print("Acceso correcto")
            print()
            print("                Bienvenido!!")
            print()
            print("-"*55)
            break
        else:
            print("Acceso denegado")     
    else:
        print("rut invalido")    
        