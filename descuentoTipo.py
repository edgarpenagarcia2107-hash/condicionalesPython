tipo = str(input("ingrese el tipo de su producto "))
precio = float(input("ingrese el valor de su producto "))

if tipo == "Textil" or tipo == "textil":
    print(f"su descuento es del 0% por lo tanto su precio es {precio}$")
elif tipo == "Electrodomestico" or tipo == "electrodomestico":
    descuento = precio * 0.037
    print(f"su descuento es del 3.7% por lo tanto su precio es {precio - descuento}$")
elif tipo == "ElementosCosina" or tipo == "elementoscosina":
    descuento = precio * 0.042
    print(f"su descuento es del 4.2% por lo tanto su precio es {precio - descuento}$")
elif tipo == "videojuegos" or tipo == "Videojuegos":
    descuento = precio * 0.078
    print(f"su descuento es del 7.8% por lo tanto su precio es {precio - descuento}$")