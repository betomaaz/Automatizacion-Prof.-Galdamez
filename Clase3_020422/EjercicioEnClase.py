#1 Realizar un prohrama que permita adquirir productos en una ferreteria
#2 El sistema debe tener una lista de productos con sus precios
#3 El sistemma debe permitir la selección del producto y calcular el valor a pagar (precio x cantidad)
#4 Cuando el cliente desee no seguir comprando, mostrar el total de la compra
#5 Luego consultar si el cliente desea despacho. Si el cliente desea despacho. Si es asim calcule el costo
#del flete según comuna de destino(no más de 5 comunas)

productos = ["1", "Alicate", 7990], ["2", "Llave inglesa", 14990], ["3", "Llave Stilson", 12990]
comunas = ["1", "Providencia", 9000], ["2", "Las Condes", 12000], ["3", "Talagante", 15000], ["4", "Ñuñoa", 5000], ["5", "Santiago", 0]
total = 0
costodespacho = 0

print("Productos disponibles")
print("{:<10} {:<20} {:<20}".format("Código", "Producto", "Precio"))


for x in productos:
    cod, prod, prec = x
    print("{:<10} {:<20} {:<20}".format(cod, prod, prec))

decision = str(input("¿Desea realizar una compra? (si/no) "))

if decision == "si":
    prod = int(input("Digite codigo de producto que desea comprar: "))-1
    cant = int(input("Ingrese cantidad del producto: "))
    prec = int(productos[prod][2])
    compra = int(prec * cant)

    print("Monto: ", compra)

    total = total + compra

    decision = str(input("¿Desea agregar productos? (si/no) "))    

    while decision == "si":
        prod = int(input("Digite codigo de producto que desea comprar: "))-1
        cant = int(input("Ingrese cantidad del producto: "))
        prec = int(productos[prod][2])
        compra = int(prec * cant)

        print("Monto: ", compra)

        total = total + compra
    
        decision = str(input("¿Desea agregar productos? (si/no) "))
        
        if decision == "no" and total > 0:
            print("El monto total de tu compra es $", total)
            
            consultaDespacho = str(input("¿Requiere despacho? (si/no) "))
            
            if consultaDespacho == "si": 
                print("Costo de despacho")
                print("{:<10} {:<20} {:<20}".format("Código", "Comuna", "Costo"))

                for x in comunas:
                    cod, com, cost = x
                    print("{:<10} {:<20} {:<20}".format(cod, com, cost))

                comuna = int(input("Ingrese código de comuna de despacho según tabla mostrada: "))-1
                costodespacho = int(comunas[comuna][2])
                print("El costo de la comuna seleccionada es $", costodespacho)

                print("El monto total de tu pedido es $", total + costodespacho)
            else:
                print("Su compra será preparada para retiro en tienda")
            



