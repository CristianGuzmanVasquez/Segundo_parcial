"""
1- desarrolle un programa en python que permita calcular el valor final del estacionamiento de motos y del candado para el centro civico que ofrese 
descuento para el guardado de su moto mensual segun los dias de uso, valor base: motocicleta 15.000 mesuales, candados: 9.000 mensuales realizar una 
tabla donde tendra dias de uso, estudiante y descuento. Ademas el candado tiene una regla adicional los estudiantes obtienen un descuento del 12% adicional por un pago con 
tarjeta de credito, si ademas la cantidad de dias es menor a 15 obtendra solo un 15%, si la cantidad de dias es menor a 10 el descuento es 0

--------------------------------------------------------
CANTIDAD DE DIAS        ESTUDIANTE        DESCUENTOS
     >= 20                 si               25%
     >= 20                 no               15%
    10<=20                 si               15%
      >=20                 no               8%
--------------------------------------------------------

2- desarrolle un programa en python que permita ingresar dos numeros enteros que indique un rango de numeros, el primero debe ser menor al segundo, luego el programa debe generar 
un numero aleatroio (al azar) entre el rando de los numeros. from random import randint, N=randint() (n1,n2). La linea 1 le permite cargar la funcion randint, la linea n2
usa la funcion randint que permite generar un numero aleatorio entre los dos valores, a modo de ejemplo randint(1,10): que numero aleatorio debe generar entre el 1 y el 10.
Un generador de numero aleatorio debe ajustar el numero para que el valor final sea adivinado  por el usuario luego de 3 intentos. Si el numero ajustado llega a quedar 
fuera del rango entonces el numero final debe dividirce por el limite inferior 
"""
import random

def numero_random():
    numero_secreto=random.randint(n1,n2)
    intentos=0
print("ingresa dos valores")
print("Adivina el numero")
while True:
    n1=int(input("n1: "))
    n2=int(input("n2: "))
    try:
        if n1>0 and n2>0:
            intentos=int(input("que numero es?: "))
            intentos +=1
             

