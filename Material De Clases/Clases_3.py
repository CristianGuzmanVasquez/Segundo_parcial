# Solicitar el nombre

nombre=input("Por favor, dime tu nombre: ")

#Lista
notas=[]

for i in range(3):
    nota=float(input(f"Ingrese la nota N {i + 1}: "))
    notas.append(nota)

suma=0
for nota in notas:
    suma= suma+nota
promedio= suma / len(notas)

estudiante={
    "nombre" : nombre,
    "notas" : notas,
    "promedio" : promedio
}

# Mostrar

print("\nResumen")
print("_"*17)
print("Nombre:", estudiante["nombre"])
print("Nota:", estudiante["notas"])
print(f"Promedio:{promedio:.1f}")
