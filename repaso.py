print("--------------Bienvenido Banco Falabella-----------------")
# Validacion de RUT

while True:
    rut = input("Ingrese su Rut (Sin punto ni guion): ")
    if rut.isdigit() and len(rut)==8:
        break
    else:
        print("El rut, solo debe tener 8 digitos numericos")
# Valida codigo de verificacion

while True:

    dv= input("Ingrese su digito verifivador: ").upper()

    if len(dv) == 1 and (dv.isdigit()) or dv == "K":
        break
    else:
        print("Error")
# Nombre     

nombre=input("Ingrese su nombre: ")

# Validar compra
while True:
    montos=input("Ingrese el monto de la compra: ")
    if montos.isdigit():
        monto=int(montos)
        if monto >= 0:
            break
        else:
            print("Error, el monto es negativo.")
    else:
        print("Error, Ingresa solo numeros")   
# Calculo de descuento 
if monto < 10000:
    descuento = 0
    porcentaje = 0
elif monto <= 50000:
    descuento = monto * 0.10
    porcentaje = 10
else:
    descuento = monto * 0.20
    porcentaje = 20    
                   
total = monto - descuento
Total=int(total)
# Boleta
print("----------------Boleta de compra---------------") 
print()
print(f"Nombre: {nombre}") 
print(f"Rut: {rut}-{dv}") 
print(f"Monto de la compra: ${monto}")
print(f"Descuento del: {porcentaje}%")
print(f"Monto total a pagar: ${Total}")
print()
print("-"*50)               