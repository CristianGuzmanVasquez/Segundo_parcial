
while True:

    Usuario=input("Ingrese su usuario: ")
    if Usuario == "Alumno_duoc":
      print(f"Hola, {Usuario}")
    else:
      print("Por favor ingrese un usuario valido")
      break

    Clave=int(input("Ingrese su clave: "))
    if Clave == 151516:
      print("Clave Correcta, Bienvenido!")
    else:
     print("clave invalida")  