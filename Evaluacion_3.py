def menu():
    print("Bienvenido al sistema de pedidos Sushi Delivery")
    while True:
        can_Pikachu=0
        can_Otaku=0
        can_Pulpo=0
        can_Anguila=0

        while True:
            print("----Menu----")
            print("\n1. Pikachu Roll $4.500\n2.Otaku Roll $5.000")
            print("\n3. Pulpo Venenoso Roll $5.200\n4. Anguila Electrica Roll $4.800")
            print("\n5. Terminar pedido")
            opcion=input("Selecciona una opcion: ")
            if opcion=="1":
                can_Pikachu+=1
                "- Pikacachu Roll, agregado al pedido"
            elif opcion=="2":
                can_Otaku*=1
                "- Otaku Roll, agregado al pedido"
            elif opcion=="3":
                can_Pulpo+=1
                "- Pulpo Venenoso Roll, agrgado al pedido"
            elif opcion=="4":
                can_Anguila+=1
                "- Anguila Electrica Roll, agregado al pedido"
            elif opcion=="5":
                total_Productos= can_Pikachu+can_Otaku+can_Pulpo+can_Anguila
                if total_Productos==0:
                    "Tu canasta esta vacia, ingresa productos"
                continue

                subtotal=(can_Pikachu*4500)+(can_Otaku*5000)+(can_Pulpo*5200)+(can_Anguila*4800)
                descuento=0
                volver_al_menu= False  






            else:
                "Ingrese una opcion valida del 1 al 5"                    