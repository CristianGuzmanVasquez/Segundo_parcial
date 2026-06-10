"""
desarrolle un programa en python que solicite una lista de numeros enteros separados por espacios valide que los numeros sean enteros,
separe los numeros pares de los inpares, muestra ambas listas y utilize por lo menos una funcion.
"""

def separar_pares_impares(lista_numeros):
    pares = [ num for num in lista_numeros if num %2==0]
    impares = [num for num in lista_numeros if num %2!=0]
    return pares, impares

print("*"*5+" Clasificador de numero pares e impares "+"*"*5)
while True:
    numeros = input("Ingrese una lista de numeros emteros, usande espacios: ")
    elementos= numeros.split()
    try:
        numeros_enteros = [int(x) for x in elementos]
        if not numeros_enteros:
            print("Error, no ingreso ningun numero, intenta de nuevo.\n")
            continue
        break
    except ValueError:
        print("Error,ingresa solo numeros enteros separados por espacios.\n")

lista_pares, lista_impares = separar_pares_impares(numeros_enteros)

print("\n----Resultados----")
print(f"Lista original: {numeros_enteros}")
print(f"Numeros pares: {lista_pares}")
print(f"Numeros impares: {lista_impares}")

            