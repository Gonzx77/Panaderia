Username = input("Hola, bienvenido a nuestra panaderia, ingrese su nombre: ")

panaderia = {
    'panesSalados': {"productos":list([
        {"nombre":"Baguette","valor":3000},
        {"nombre":"Pan de campo", "valor":2500},
        {"nombre":"Pan de centeno","valor":3500},
        {"nombre":"Pan de ajo","valor":1000},
        {"nombre":"Pan de molde integral","valor":3000},
        {"nombre":"Pan de queso","valor":1500},
        {"nombre":"Pan de aceitunas","valor":3000},
        {"nombre":"Bollos de pizza","valor":3500},
        {"nombre":"Pan de cebolla","valor":2000},
        {"nombre":"Pan de maíz","valor":2000}])},
    'panesDulces': {"productos":list([
        {"nombre":"Croissant","valor":3000},
        {"nombre":"Rosca de Reyes","valor":3000},
        {"nombre":"Pan de muerto","valor":3000},
        {"nombre":"Pan de canela","valor":3000},
        {"nombre":"Pan de banana","valor":6000},
        {"nombre":"Pan de zanahoria","valor":3000},
        {"nombre":"Donas","valor":3000},
        {"nombre":"Pan de jengibre","valor":3000},
        {"nombre":"Conchas","valor":3000},
        {"nombre":"Churros","valor":3000}])},
    'postres': {"productos":list([
        {"nombre":"Tarta de manzana","valor":3000},
        {"nombre":"Cupcakes","valor":3000},
        {"nombre":"Galletas decoradas","valor":3000},
        {"nombre":"Pastel de zanahoria","valor":3000},
        {"nombre":"Brownies","valor":3000},
        {"nombre":"Cheesecake","valor":3000},
        {"nombre":"Macarons","valor":3000},
        {"nombre":"Éclairs","valor":3000},
        {"nombre":"Tarta de frutas","valor":3000},
        {"nombre":"Donas","valor":3000}])},
    'promociones': {"descuentos":list([
        {"nombre":"Donas","valor":0.15},
        {"nombre":"Pan de banana","valor":0.15},
        {"nombre":"Galletas decoradas","valor":0.15},
        {"nombre":"Pan de molde","valor":0.15},
        {"nombre":"Pan de cebolla","valor":0.15}])}
}

op2 = 0
montoTotal = 0
factura = None
facturaFinal = []


while op2 == 0:
    print(f"""
    0: Panes Salados
    1: Panes Dulces
    2: Postres""")

    op1 = int(input("\n Ingresa la categoria a la que desea acceder: "))

    if op1 == 0:
        print("Haz seleccionado: Panes Salados")
        op1 = "panesSalados"
    elif op1 == 1:
        print("Haz seleccionado: Panes Dulces")
        op1 = "panesDulces"    
    elif op1 == 2:
        print("Haz seleccionado: Postres")
        op1 = "postres"
    else:
        print("Este producto no existe")

    for indice, producto in enumerate(panaderia[op1]["productos"]):
        name = producto["nombre"]
        value = producto["valor"]
        print(f"""{indice} {name}, valor: {value}""")

    op2 = int(input("\n Ingresa el numero del producto a comprar: "))

    selectedProduct = panaderia[op1]["productos"][op2]
    selectedProductName = selectedProduct["nombre"]
    selectedProductValue = selectedProduct["valor"]

    compra = (f"""Haz seleccionado el producto {selectedProductName}, con un valor de: {selectedProductValue}""")
    print(compra)

    descuentosName = [descuento["nombre"] for descuento in panaderia["promociones"]["descuentos"]]
    descuentoValue = None
    for descuento in panaderia["promociones"]["descuentos"]:
        if descuento["nombre"] == selectedProductName:
            descuentoValue = descuento["valor"]
            break

    if selectedProductName in descuentosName:
        print(f"""¡ Este producto tiene promocion !: Compre 3 con un 15% de descuento al total de la compra""")
        op3 = input("Desea comprar la oferta?: ")
        if op3.lower() == "si":
            promo = "Si (-15% cada 3 unidades)"
            cantidad = int(input("Cuantas promociones desea comprar?: "))
            total1 = int(selectedProductValue * 3)
            monto  = int(total1 - (total1 * descuentoValue))
            print(f"""Sumado al la factura ({monto})""")
                
        elif op3.lower() != "si":
            promo = "No"
            cantidad = int(input("Cuantos desea comprar?: "))
            total1 = ((selectedProductValue) * cantidad)
            print(f"""Sumado al la factura ({total1})""")
            monto = total1
    else:
        promo = "No"
        cantidad = int(input("Cuantos desea comprar?: "))
        total1 = ((selectedProductValue) * cantidad)
        print(f"""Sumado al la factura ({total1})""")
        monto = total1
        
    montoTotal += monto
    
    factura = (f"""Nombre:{selectedProductName}, ¿Promocion?:{promo}, Precio(Unidad):{selectedProductValue}, Cantidad:{cantidad}, Precio:{monto}""")
    facturaFinal.append(factura)
    

    op4 = input("Desea comprar otro producto?: ")
    
    if op4.lower() == "si":
        op2 = 0
        
    else:
        print(f""" FACTURA Nombre: {Username} \n""")
        for item in facturaFinal:
            print(f"""- {item}""")
        print("\n")
        
        pago = 0
        while pago == 0:
            print(f"""El total de su compra es de: {montoTotal}""")
            money = int(input("Ingrese su pago: "))
            if money >= montoTotal:
                cambio = money - montoTotal
                print(f"""Tu cambio es de: {cambio}""")
                print("\n¡Gracias por tu compra!")
                pago = pago + 1

            else:
                falta = montoTotal - money
                print(f"""El dinero no es suficiente, te hace falta: {falta}""")
                pago = 0
            op2 = 1