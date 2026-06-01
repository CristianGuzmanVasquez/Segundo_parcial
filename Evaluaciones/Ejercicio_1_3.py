
comandante_Galactico=0
cadete_Estelar=0
while True:
    print("*"*20+"Academia De Pilotos Estelares"+"*"*20)
    try:
        Pilotos=int(input("\nIngrese el numero de pilotos ha registrar: "))
        if Pilotos>0:
            break
        else:
            print("Ingrese un numero superiro a 0 para continuar el entrenamiento.")
    except ValueError:
        print("¡Número inválido! Ingresa un entero positivo para continuar el entrenamiento.")

for i in range(Pilotos):
    print(f"\nRegistro del piloto numero {i+1} de {Pilotos} ")
    while True:
        nombre_Piloto=input("Ingrese la identificacion del piloto: ")
        if len(nombre_Piloto) >=6 and " " not in nombre_Piloto:
            break
        else:
            print("Identificacion Invalida!, debe tener minimo 6 caracteres.")

    while True:
        try:
            nivel_Vuelo=int(input(f"Ingrese el nivel de vuelo del piloto {nombre_Piloto}: "))
            if nivel_Vuelo>40:
                comandante_Galactico+=1
                print(f"El piloto {nombre_Piloto} sera nombrado como Comandante Galactico.")
            elif nivel_Vuelo <=0:
                print("Ingrese un numero entero positivo")
                continue    
            else:
                cadete_Estelar+=1
                print(f"El piloto {nombre_Piloto} sera nombrado como Cadete Estelar")
            break 
        except ValueError:
            print("Ingrese solo numeros enteros positivos")
 
print(f"\nLa flota estelar cuenta con {comandante_Galactico} Comandantes Galacticos y {cadete_Estelar} Cadetes Estelares.\n¡Prepárense para despegar! ")
    


