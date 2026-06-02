"""
Registro de calificaciones, el programa debe permitir ingresar 5 calificaciones de 5 asignaturas, el programa debe guardar las notas dentro de una lista por cada asiganturas y al final generar 
el promedio final del estudiante y toda la informacion debe guardarse en un diccionario el cual servira para generar un resumen.  
"""
calificaciones = {}

def registro_Asignaturas():
    while True:
        asignatura = input("Ingrese la asignatura que desea registrar (o ingrese 'X' para salir): ").strip()
        if asignatura.upper() == 'X':
            break
        calificaciones[asignatura] = []

def registrar_Notas():
    if not calificaciones:
        print("Primero debe registrar asignaturas")
        return

    asignatura = input("Escriba la asignatura para registrar las notas: ").strip()

    if asignatura not in calificaciones:
        print("La asignatura no existe")
        return

    while True:
        try:
            nota = float(input(f"Ingrese una nota para {asignatura} (o -1 para salir): "))
            
            if nota == -1:
                break
            elif 1 <= nota <= 7:
                calificaciones[asignatura].append(nota)
            else:
                print("Ingrese una nota entre 1 y 7")
        except ValueError:
            print("Error, ingrese un numero valido")

def registro_Promedio():
    if not calificaciones:
        print("No hay asignaturas registradas")
        return

    for asignatura, notas in calificaciones.items():

        if notas:
            promedio = sum(notas) / len(notas)
            print(f"Asignatura: {asignatura} | Notas: {notas} | Promedio: {promedio:.2f}")
        else:
            print(f"Asignatura: {asignatura} | Sin calificaciones registradas")

print("¡Bienvenido al sistema de registro de calificaciones!\n")

while True:

    print("=" * 7 + " SISTEMA DE CALIFICACIONES " + "=" * 7)
    print("\n1. Ingresar asignaturas")
    print("2. Ingresar notas")
    print("3. Ver registro de notas")
    print("4. Salir")

    try:
        opcion = int(input("Seleccione una opcion: "))

        if opcion == 1:
            registro_Asignaturas()
        elif opcion == 2:
            registrar_Notas()
        elif opcion == 3:
            registro_Promedio()
        elif opcion == 4:
            print("Saliendo del sistema...")
            break
        else:
            print("Ingrese una opción válida")
    except ValueError:
        print("Ingrese un número del 1 al 4")