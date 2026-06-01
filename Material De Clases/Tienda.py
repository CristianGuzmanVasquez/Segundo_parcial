"""
suma = 0
for i in range(5):
    while True:
        try:
            numero=float(input(f"Ingrese el nuemro {i+1}: "))
            suma=int(suma + numero)
            break
        except:
            print("Error, Debe ingresar un numero")
print("La suma total es:",suma)
"""            
"""
tenemos una pequeña tienda que desea moderniazar su sistema de venta, actualmente el vendedor lleva un modesto registro manual y al final del dia debe calcular todo lo vendido;
para facilitar el trabajo debemos crear un programa en python que guarde las compras  y cuando hagamos la venta debe solicitar sus datos, nombre y rut, una ves que tengamos todos los datos el usuario 
debe introducir 10 productos para comprar, una ves realizada la compra, debe mostrar el resultado de la compra si tiene algun descuento muestra el descuento mas iva, tipo boleta 
"""
