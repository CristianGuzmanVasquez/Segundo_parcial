def main():
    print("Bienvenido al sistema de pedidos de Sushi Delivery")
    
    # Bucle principal para permitir múltiples pedidos en una sesión
    while True:
        # Inicializamos los contadores de cada producto para el pedido actual
        cant_pikachu = 0
        cant_otaku = 0
        cant_pulpo = 0
        cant_anguila = 0
        
        # Bucle del menú de selección de productos
        while True:
            print("\n--- MENÚ DE ROLLS ---")
            print("1. Pikachu Roll ($4500)")
            print("2. Otaku Roll ($5000)")
            print("3. Pulpo Venenoso Roll ($5200)")
            print("4. Anguila Eléctrica Roll ($4800)")
            print("5. Terminar pedido y pagar")
            
            opcion = input("Seleccione una opción (1-5): ")
            
            if opcion == '1':
                cant_pikachu += 1
                print("✔ Pikachu Roll agregado al pedido.")
            elif opcion == '2':
                cant_otaku += 1
                print("✔ Otaku Roll agregado al pedido.")
            elif opcion == '3':
                cant_pulpo += 1
                print("✔ Pulpo Venenoso Roll agregado al pedido.")
            elif opcion == '4':
                cant_anguila += 1
                print("✔ Anguila Eléctrica Roll agregado al pedido.")
            elif opcion == '5':
                # Validar que al menos haya pedido un producto
                total_productos = cant_pikachu + cant_otaku + cant_pulpo + cant_anguila
                if total_productos == 0:
                    print("Su pedido está vacío. Por favor agregue al menos un producto.")
                    continue
                
                # Proceso de descuento
                subtotal = (cant_pikachu * 4500) + (cant_otaku * 5000) + (cant_pulpo * 5200) + (cant_anguila * 4800)
                descuento = 0
                volver_al_menu = False
                
                while True:
                    tiene_codigo = input("¿Posee un código de descuento? (s/n): ").lower()
                    if tiene_codigo == 's':
                        while True:
                            codigo = input("Ingrese el código (o teclee 'X' para volver al menú de productos): ")
                            if codigo == "soyotaku":
                                descuento = subtotal * 0.10
                                print("¡Descuento del 10% aplicado exitosamente!")
                                break # Rompe el bucle de ingreso de código
                            elif codigo.upper() == "X":
                                volver_al_menu = True
                                break # Rompe el bucle de ingreso de código
                            else:
                                print("Código no válido.")
                        break # Rompe el bucle de la pregunta 's/n'
                    elif tiene_codigo == 'n':
                        break # Rompe el bucle de la pregunta 's/n'
                    else:
                        print("Por favor, responda con 's' para sí, o 'n' para no.")
                
                # Si el usuario eligió 'X', volvemos a mostrarle el menú principal de rolls
                if volver_al_menu:
                    continue
                
                # Si llegamos aquí, el pedido está listo para ser mostrado
                total_pagar = subtotal - descuento
                
                # Impresión del detalle del pedido con el formato solicitado
                print("\n" + "*"*30 + f"\n TOTAL PRODUCTOS:{total_productos}")
                print("*"*30)
                print(f"Pikachu Roll : {cant_pikachu}\nOtaku Roll : {cant_otaku}")
                print(f"Pulpo Venenoso Roll: {cant_pulpo}\nAnguila Eléctrica Roll: {cant_anguila}")
                print("*"*30)
                print(f"Subtotal por pagar: ${int(subtotal)}")
                print(f"Descuento por código: ${int(descuento)}")
                print(f"TOTAL: ${int(total_pagar)}")
                
                break # Rompe el bucle del menú de selección para preguntar si desea otro pedido
                
            else:
                print("Opción no válida. Por favor, ingrese un número del 1 al 5.")
        
        # Al finalizar el recibo, preguntamos si desea realizar otro pedido general
        nuevo_pedido = input("\n¿Desea realizar otro pedido o salir del programa? (ingrese 'salir' para terminar o cualquier otra tecla para nuevo pedido): ").lower()
        if nuevo_pedido == 'salir':
            print("¡Gracias por su compra en Sushi Delivery! Hasta pronto.")
            break

# Punto de entrada de la aplicación
if __name__ == "__main__":
    main()