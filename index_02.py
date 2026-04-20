#Lista
"""
numero=[1,2,3,4,5]
print(numero[0])

numero.append(50)
print(numero)

"""
#Tupla
"""
objetos=("lentes","Mesa","Cereza")
print(objetos[0])

"""
#Diccionario
"""
Cosas={
    "Juan":25,
    "Maria":20,
    "Carlos":19,
}
print("Hola Carlos tienes una edad de:",Cosas["Carlos"],", Hola Juan tienes una edad de:",Cosas["Juan"])  
"""
#___________________________________________________________________________________________________________#

#Funciones
"""
def saludo(nombre):
   return f"¡Hola!, {nombre}"
mensaje=saludo("Juan.")
print(mensaje)
"""

def saludo(nombre):
    return "¡Hola!", nombre + "!"
mensaje=saludo("bienvenido ",nombre)
nombre=input("Dime tu nombre: ")
print(f"{},{}")