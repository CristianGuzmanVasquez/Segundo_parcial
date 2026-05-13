"""
def nombre_Funcion():
    print("mensaje")

# def palabra reservada 
# nombre_Funcion
# () Parametro
# : Inicio del bloque
# Identacion 
"""
def suma(a,b):
    return a+b
def resta(a,b):
    return a-b
def multiplicacion(a,b):
    return a*b
def divicion(a,b):
    if b==0:
        return "Error, no se puede dividir por cero"
    return a/b

print("\n===========Calculadora===========\n")

num1= float(input("Ingresa tu primer numero: "))
num2= float(input("Ingresa tu segundo numero: "))
print("\n1. Sumar\n2. Resta\n3. Multiplicar\n4. Dividir")
opcion=input("\nSelecciona una opcion: ")
if opcion=="1":
    print("Resultado:",suma(num1,num2))
elif opcion=="2":
    print("Resultado:",resta(num1,num2))
elif opcion=="3":
    print("Resultado:",multiplicacion(num1,num2))
elif opcion=="4":
    print("Resultado", divicion(num1,num2))
else:
    print("Ingrese una opcion valida") 
