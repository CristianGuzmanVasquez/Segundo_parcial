def main():
    print("Bienvenido al sistema de pedidos Sushi Delivery")
    while True:
        can_Pikachu=0
        can_Otaku=0
        can_Pulpo=0
        can_Anguila=0

        while True:
            print("-----------Menu-----------")
            print("\n1.Pikachu Roll $4.500\n2.Otaku Roll $5.000")
            print("3.Pulpo Venenoso Roll $5.200\n4.Anguila Electrica Roll $4.800")
            print("5.Terminar pedido")
            opcion=input("Selecciona una opcion: ")
            if opcion=="1":
                can_Pikachu+=1
                print("- Pikacachu Roll, agregado al pedido")
            elif opcion=="2":
                can_Otaku*=1
                print("- Otaku Roll, agregado al pedido")
            elif opcion=="3":
                can_Pulpo+=1
                print("- Pulpo Venenoso Roll, agrgado al pedido")
            elif opcion=="4":
                can_Anguila+=1
                print("- Anguila Electrica Roll, agregado al pedido")
            elif opcion=="5":
                total_Productos= can_Pikachu + can_Otaku + can_Pulpo + can_Anguila
                if total_Productos==0:
                    print("Tu canasta esta vacia, ingresa productos")
                    continue

                subtotal=(can_Pikachu*4500)+(can_Otaku*5000)+(can_Pulpo*5200)+(can_Anguila*4800)
                descuento=0
                volver_al_menu= False  

                while True:
                    tiene_codigo=input("posee un codigo de descuento? (s/n): ").lower()
                    if tiene_codigo=="s":
                        while True:
                            codigo=input("Ingrese el codigo o precione X para volver al menu: ")
                            if codigo=="soyotaku":
                                descuento=subtotal*0.10
                                print("Descuento del 10% aplicado exitosamente!!")
                                break
                            elif codigo.upper()=="X":
                                volver_al_menu==True
                                break
                            else:
                                print("Codigo no valido") 
                        break                                            
                    elif tiene_codigo=="n":
                        break
                    else:
                        print("Por favor, responda con 's' para sí, o 'n' para no.")
            
                if volver_al_menu:
                    continue 
                total_pagar=subtotal-descuento
            
                print("\n"+"*"*30+f"\nTOTAL PRODUCTOS: {total_Productos}")
                print("*"*30)
                print(f"Pikachu Roll: {can_Pikachu}\nOtaku Roll: {can_Otaku}")
                print(f"Pulpo Venenoso Roll: {can_Pulpo}\nAnguila Electrica Roll: {can_Anguila}")
                print("*"*30)
                print(f"Subtotal por pagar: ${int(subtotal)}")
                print(f"Descuento por codigo: ${int(descuento)}")
                print(f"TOTAL: ${int(total_pagar)}")
                break
            else:
                print("Ingrese una opcion valida del 1 al 5")

        nuevo_pedido=input("Desea realizar otro pedido o salir del programa?\n(Ingrese 'salir' para terminar o cualquier otra tecla para nuevo pedido): ").lower()
        if nuevo_pedido=="salir":
            print("Geacias por comprar, vuelva pronto!!")
            break

if __name__=="__main__":
    main()                                   