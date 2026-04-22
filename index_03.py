# TRY

"""
try:
    resultado=10/0
except ZeroDivisionError:
    print("¡Error! No debemos dividir entre cero.")
finally:
    print("Bloque Finalizado")    
"""
try:
    num1=float(input("Por favor, ingresa un numero: "))
    num2=float(input("Por favor, ingresa un numero: "))
    
    if num2==0:
        raise ZeroDivisionError#Lanza el error o proboca el error
    resultado=num1/num2
    print(f"El resultado de esta divicion es:{resultado}")    
except ValueError:
    print("¡ERROR! Ingresa un nuevo numero")
except ZeroDivisionError:
    print("¡ERROR! No se puede dividir entre cero.")
  
print("Fin del programa")      

#Actividad
"""
Estimado estudiante usted ha sido seleccionado para realizar la interfaz de usuario de los cajeros automaticos del grupo santander 
el programa debe solicitar al usuario numero de rut, el cual debe ser validado con su numero de verificacion posteriormente 
el ususario debe introducir su clave que no debe ser mayor o menor a diez digitos. ¡Suerte!

"""