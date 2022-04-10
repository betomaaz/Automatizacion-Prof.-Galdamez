#1 Realizar un prohrama que permita adquirir productos en una ferreteria
#2 El sistema debe tener una lista de productos con sus precios
#3 El sistemma debe permitir la selección del producto y calcular el valor a pagar (precio x cantidad)
#4 Cuando el cliente desee no seguir comprando, mostrar el total de la compra
#5 Luego consultar si el cliente desea despacho. Si el cliente desea despacho. Si es asi calcule el costo
#del flete según comuna de destino(no más de 5 comunas)


productos = ["1", "Alicate", 7990], ["2", "Llave inglesa", 14990], ["3", "Llave Stilson", 12990], ["4", "Destornillador", 6990]
comunas = ["1", "Providencia", 4000], ["2", "Las Condes", 5000], ["3", "Talagante", 7500], ["4", "Ñuñoa", 3000], ["5", "Santiago", 3000]
total = 0
costodespacho = 0
orden = []

decision = str(input("¿Desea realizar una compra? (si/no): "))

while decision != "si" and decision != "no":
    print("Solo se puede escribir 'si' o 'no' como respuesta")
    print("----------------------------------------------------------------------------")
    decision = str(input("¿Desea realizar una compra? (si/no): "))
    

while decision == "si":
            
    print("Productos disponibles")
    print("{:<10} {:<20} {:<20}".format("Código", "Producto", "Precio"))

    for x in productos:
        cod, prod, prec = x
        print("{:<10} {:<20} {:<20}".format(cod, prod, prec))

    prod = input("Digita codigo de producto que desea comprar: ")
    
    if prod.isnumeric() == True:
        P = int(prod)-1

        if P+1 >= 1 and P+1 <= len(productos):
            cant = int(input("Ingrese cantidad del producto: "))
            prec = int(productos[P][2])
            compra = int(prec * cant)

            ord = [productos[P][1], prec, compra]
            orden.append(ord)

            print("Monto: ", compra)
            total = total + compra

            decision = str(input("¿Desea agregar más productos a su compra? (si/no): "))     

            while decision != "si" and decision != "no":
                print("Solo se puede escribir 'si' o 'no' como respuesta")
                print("----------------------------------------------------------------------------")
                decision = str(input("¿Desea agregar más productos a su compra? (si/no): "))

        else:
            print("Por favor ingresa un código existente en la lista")
            decision = str(input("¿Intentar de nuevo? (si/no): "))

            while decision != "si" and decision != "no":
                print("Solo se puede escribir 'si' o 'no' como respuesta")
                print("----------------------------------------------------------------------------")
                decision = str(input("¿Intentar de nuevo? (si/no): "))
    else:
        print("Por favor ingresa un caracter numerico disponible en la lista. Letras y simbolos no permitidos.")    


if decision == "no" and total > 0:

    print("Detalle de tu compra")
    print("{:<20} {:<20} {:<20}".format("Artículo", "Precio unitario", "Total"))

    for i in orden:
        art, pre, tot = i
        print("{:<20} {:<20} {:<20}".format(art, pre, tot))

    print("El monto total de tu compra es $", total)
    
    consultaDespacho = str(input("¿Requiere despacho? (si/no): "))

    while consultaDespacho != "si" and consultaDespacho != "no":
        print("Solo se puede escribir 'si' o 'no' como respuesta")
        print("----------------------------------------------------------------------------")
        consultaDespacho = str(input("¿Requiere despacho? (si/no): "))
    
    while consultaDespacho == "si": 
        print("Costo de despacho")
        print("{:<10} {:<20} {:<20}".format("Código", "Comuna", "Costo"))

        for x in comunas:
            cod, com, cost = x
            print("{:<10} {:<20} {:<20}".format(cod, com, cost))

        comuna = input("Ingrese código de comuna de despacho según tabla mostrada: ")
    
        if comuna.isnumeric() == True:
            C = int(comuna)-1

            if C+1 >= 1 and C+1 <= len(comunas):
            
                costodespacho = int(comunas[C][2])
                print("El costo de la comuna seleccionada es $", costodespacho)
                print("----------------------------------------------------------------------------")
                print("El monto total de tu pedido + despacho es $", total + costodespacho)
                print("¡Gracias por su compra!")

            else:
                print("Por favor ingresa un código existente en la lista de comunas")
                consultaDespacho = str(input("¿Intentar de nuevo? (si/no): "))

                while consultaDespacho != "si" and consultaDespacho != "no":
                    print("Solo se puede escribir 'si' o 'no' como respuesta")
                    print("----------------------------------------------------------------------------")
                    consultaDespacho = str(input("¿Intentar de nuevo? (si/no): "))
                
                if consultaDespacho == "no":
                    print("----------------------------------------------------------------------------")
                    print("No seleccionaste comuna de despacho. Su orden será preparada para retiro en tienda")
                    print("----------------------------------------------------------------------------")

                    break

        else:
            print("Por favor ingresa un caracter numerico disponible en la lista de comunas. Letras y simbolos no permitidos.")
    else:
        print("----------------------------------------------------------------------------")
        print("¡Gracias por su compra! Su orden será preparada para retiro en tienda")
        print("----------------------------------------------------------------------------")

if decision == "no" and total == 0:
    print("----------------------------------------------------------------------------")
    print("¡Hasta pronto!")
    print("----------------------------------------------------------------------------")