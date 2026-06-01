import math
while True:
    
    def validar_nombre():
        while True:
            nombre = input("Ingrese su nombre: ").strip()
            if len(nombre) >= 3 and nombre.replace(" ", "").isalpha():
                return nombre
            else:
                print("Error: El nombre debe tener al menos 3 letras.")

    def validar_telefono():
        while True:
            telefono = input("Ingrese su teléfono (8 o 9 dígitos): ")
            if telefono.isdigit() and len(telefono) in [8, 9]:
                return telefono
            else:
                print("Error: Teléfono inválido.")

    def validar_numero(mensaje):
        while True:
            try:
                valor = float(input(mensaje))
                if valor > 0:
                    return valor
                else:
                    print("Error: El valor debe ser mayor que 0.")
            except:
                print("Error: Ingrese un número válido.")
            
    def main():
        print("========= SISTEMA DE TRANSPORTE ==========")

        nombre = validar_nombre()
        telefono = validar_telefono()

        print("\nIngrese dimensiones de la caja en cm:")
        largo = validar_numero("Largo (cm): ")
        ancho = validar_numero("Ancho (cm): ")
        alto = validar_numero("Alto (cm): ")

        cantidad_cajas = int(validar_numero("Cantidad de cajas: "))

        # Convertir a metros
        largo_m = largo / 100
        ancho_m = ancho / 100
        alto_m = alto / 100

        # Volumen por caja
        volumen_caja = largo_m * ancho_m * alto_m

        # Capacidad del camión
        capacidad_camion = 29  # m³

        # Cajas por camión
        cajas_por_camion = capacidad_camion / volumen_caja

        # Camiones necesarios (redondeo hacia arriba)
        camiones = math.ceil(cantidad_cajas / cajas_por_camion)

        # Precio
        precio_camion = 150000
        total = camiones * precio_camion

    
        print("\n************ Boleta ************")
        print(f"Cliente: {nombre}")
        print(f"Teléfono: {telefono}")
        print(f"Cantidad de cajas transportadas: {cantidad_cajas}")
        print(f"Camiones necesarios: {camiones}")
        print(f"Valor total: ${total:,}".replace(",", "."))
        print()  
    main()
    respuesta=input("Desea realizar otra cotizacion?(s/n): ").lower()
    if respuesta=="n":
        print("Hasta luego!!")
        break