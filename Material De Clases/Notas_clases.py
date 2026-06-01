"""
Registro de calificaciones, el programa debe permitir ingresar 5 calificaciones de 5 asignaturas, el programa debe guardar las notas dentro de una lista por cada asiganturas y al final generar 
el promedio final del estudiante y toda la informacion debe guardarse en un diccionario el cual servira para generar un resumen.  
"""

asignaturas=[
    "Matematica",
    "Lenguaje",
    "Ciencias",
    "Historia",
    "Programacion"
]

notas={}

def validar_Nota():
    while True:
        try:
            nota=float(input("Ingrese notas: "))
            if 1<= nota <=7:
                return nota
            else:
                print("La nota solo debe ser del 1 al 7")
        except ValueError:
            print("Error, debe ingresar un numero valido")

def ingresar_Notas():
    print("\n-----Ingreso de notas-----")
    for asignatura in asignaturas:
        print(f"\nAsignatura: {asignatura}")
        nota=validar_Nota()
        notas[asignatura]=nota
        print("\nNotas guardadas correctamente")

def consultar_Notas ():
    print("\n-----Calificaciones-----")
    if not notas:
        print("No tiene notas registradas")
        return
    for asignatura, nota in notas.items():
        print(f"{asignatura}: {nota}")

def calcular_Promedio():
    if not notas:
        print("No tiene notas registradas")
        return
    promedio= sum(notas.values()) / len(notas)
    print(f"\nPromedio general: {promedio:.f}")

while True:
    print("=====")            