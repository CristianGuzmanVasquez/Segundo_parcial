from random import randint

while True:
    
    num1=int(input("Ingrese el limite inferior: "))
    num2=int(input("Ingrese el limite superior: "))
    if num1 >= num2:
        print("Error, El limite inferior debe ser menor al superior")
    else:
        break    

while True:
 # Numero aleatorio.

    numero = randint(num1,num2)  

 # Ajuste en multiplo de 3 

    ajustado=(numero//3)*3

    if ajustado < num1:
        ajustado = num1

 #Intento 1
    intento1=int(input("Intenta adivinar: "))

    if intento1 == ajustado:
        print("Felicitaciones, adivino en el primer intento")
        break
    else:
        if intento1 < ajustado:
            print("El numero es mayor")
        else:
            print("El numero es menor")
 # Intento 2
 
    intento2=int(input("Intenta de nuevo: "))

    if intento2 == ajustado:
        print("Felicitaciones, adivino en el segundo intento")
        break
    else:
        if intento2< ajustado:
            print("El numero es mayor")
        else:
            print("El numero es menor")
 # Pista
    print("Te dare una pista: ")
    dist1=abs (ajustado - intento1)
    dist2=abs (ajustado - intento2)

    if dist1<dist2:
        print(f"El numero que buscas es mas cercano a {intento1} que de {intento2}")
    elif dist2 < dist1:
        print(f"El numero que buscas es mas cercano a {intento2} que de {intento1}")
    else:
        print("Los dos intentos estan a la misma distancia")                    
 
 # Intento 3
    
    intento3=int(input("Este es tu ultimo intento: "))

    if intento3 == ajustado:
        print("Felicitaciones, adivino en su ultimo intento")
        break
    else:
        print("has fallado.")
        print(f"El numero era {ajustado}")
        break
       