"""
El centro de estudio duoc nos acaba de contratar para realizar un nuevo sistema de calificacion para sus estudiantes
asignatura para registrar, matematica 1, fundamento de programacion, thebox, inteligencia artificial y ciencia de datos,
el docente debe introducir las calificaciones de cada una de las asiganturas, debe ser capas de consultar las calificaciones 
y calcular el promedio .
El programa debe tener manejo de errores (Solo numeros del 1-7)
"""

asignaturas=[
    "Matematica 1",
    "Fundamentos de Programacion",
    "TheBox",
    "Inteligencia Artificial",
    "Ciencia de Datos"
]
notas={}

def validar_nota():
    while True:
        try:
            nota=float(input("ingrese nota (solo 1.0 al 7.0): "))
            if 1<= nota <= 7:
                return nota
            else:
                print("La nota solo debe ser del 1 al 7")
        except ValueError:
            print("Error, debe ingresar un numero valido")

def ingresar_notas():
    print("\n----Ingreso de notas----")
    for asignatura in asignaturas:
        print(f"\nasignatura: {asignatura}")
        nota=validar_nota()
        notas[asignatura] = nota
        print("\nNotas guardadas correctamente")

def consultar_notas():
    print("\n----Mis calificaciones----")
    if not notas:
        print("No hay notas registradas")
        return
    for asignatura, nota in notas.items():
        print(f"{asignatura}: {nota}")

def calcular_promedio():
    if not notas:
        print("No hay notas para calcular")
        return
    promedio= sum(notas.values()) / len(notas)
    print(f"\nPromedio general: {promedio:.2f}")

def menu():
    while True:
        print("\n==== SISTEMA DE CALIFICACIONES ====")
        print("1. Ingresar calificaciones")
        print("2. Consultar calificaciones")
        print("3. Calcular promedio")
        print("4. Salir")

        try:
            opcion= int(input("Seleccione una opción: "))
            if opcion== 1:
                ingresar_notas()
            elif opcion== 2:
                consultar_notas()
            elif opcion== 3:
                calcular_promedio()
            elif opcion== 4:
                print("Saliendo del sistema") 
                break
            else:
                print("Opcion invalida")
        except ValueError:
            print("Error, Debe ingresar un numero entero")
menu()                              