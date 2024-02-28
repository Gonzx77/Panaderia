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
        {"nombre":"Pan de banana","valor":3000},
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
        {"nombre":"Donas","valor":3000}])}
}

print(f"""
0: Panes Salados
1: Panes Dulces
2: Postres""")

op1 = int(input("\n Ingresa la categoria a la que desea acceder: "))

if op1 == 0:
    print("Haz seleccionado: Panes Salados")
    for indice, producto in enumerate(panaderia["panesSalados"]["productos"]):
        name = producto["nombre"]
        value = producto["valor"]
        print(f"""{indice} {name}, valor: {value}""")
    op1 = "panesSalados"
elif op1 == 1:
    print("Haz seleccionado: Panes Dulces")
    for indice, producto in enumerate(panaderia["panesDulces"]["productos"]):
        name = producto["nombre"]
        value = producto["valor"]
        print(f"""{indice} {name}, valor: {value}""")
    op1 = "panesDulces"    
elif op1 == 2:
    print("Haz seleccionado: Postres")
    for indice, producto in enumerate(panaderia["postres"]["productos"]):
        name = producto["nombre"]
        value = producto["valor"]
        print(f"""{indice} {name}, valor: {value}""")
    op1 = "postres"
else:
    print("Este producto no existe")


op2 = int(input("\n Ingresa el numero del producto a comprar: "))

selectedProduct = panaderia[op1]["productos"][op2]
selectedProductName = selectedProduct["nombre"]
selectedProductValue = selectedProduct["valor"]

compra = (f"""Haz seleccionado el producto {selectedProductName}, con un valor de: {selectedProductValue}""")
print(compra)

if selectedProductName == "Galletas decoradas":
    print("¡ Este producto tiene promocion !: Compre 3 en 8000")
    op3 = input("Desea comprar la oferta?: ")
    if op3.lower() == "si":
        print("Perfecto, total a pagar: 8000")
        monto = 8000
        money = int(input("\n Ingrese su pago: "))
        if money >= monto:
            cambio = money - monto
            print(f"""Tu cambio es de: {cambio}""")
            print("\n¡Gracias por tu compra!")

        else:
            falta = monto - money
            print(f"""El dinero no es suficiente, te hace falta: {falta}""")
            
elif selectedProductName == "Bollos de pizza":
    print("¡ Este producto tiene promocion !: Compre 3 en 9000")
    op3 = input("Desea comprar la oferta?: ")
    if op3.lower() == "si":
        print("Perfecto, total a pagar: 9000")
        monto = 9000
        money = int(input("\n Ingrese su pago: "))
        if money >= monto:
            cambio = money - monto
            print(f"""Tu cambio es de: {cambio}""")
            print("\n¡Gracias por tu compra!")

        else:
            falta = monto - money
            print(f"""El dinero no es suficiente, te hace falta: {falta}""")

            


    else:
        print(f"""Bien, total a pagar: {selectedProduct["valor"]}""")
        monto = selectedProduct["valor"]
        money = int(input("\n Ingrese su pago: "))

        if money >= monto:
            cambio = money - monto
            print(f"""Tu cambio es de: {cambio}""")
            print("\n¡Gracias por tu compra!")

        else:
            falta = monto - money
            print(f"""El dinero no es suficiente, te hace falta: {falta}""")