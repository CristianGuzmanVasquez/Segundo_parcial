print("----------ARRIENDO DE EQUIPOS------------")
nombre=input("Ingrese su nombre: ")
while True:
    if len(nombre) >= 3:
        break
    else:
        print("Su nombre debe tener minimo 3 caracteres")
telefono= input("Ingrese su telefono: ") 
while True:
    if telefono.isdigit() and len(telefono) == 8:
        break
    else:
        print("Ingrese su numero sin el +569") 
hora_trabajo=input("Ingrese las horas de trabajo: ")
while True:
    if hora_trabajo.isdigit():
        Horas= int(hora_trabajo)
        break
    else:
        print("Ingrese solo numeros") 
print("Que equipo desea arrendar")  
print()
print("1- Excavadora ($200.000/hora)")
print("2- Grua ($250.000/hora)")
print("3- Mezcaldora ($150.000/hora)")
opcion=input("Seleccione una opcion: ")
while True: 
    if opcion.isdigit() and len(opcion) == 1:
        break
    else: 
        print("Ingrese solo un numero")
if opcion == 1:
    "200000"
elif opcion == 2:    
    250000
elif opcion== 3:    
    150000
else:
    print("Ingrese una opcion valida")    
Total=opcion*hora_trabajo 
 
print("----------Boleta---------")
print(f"Nombre: {nombre}")
print(f"Numero de telefono:+569 {telefono} ")
print(f"total de horas: {hora_trabajo}")
#print(f"Equipo selecionado: {maquina}")
print(f"Monto a pagar: ${Total}")

