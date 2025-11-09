i = float(input("ingrese el valor de su articulo "))
if i > 150000:
    descuento = 0.05 
    print(f"el valor de descuanto de su articulo es -> {i * descuento}")
    print(f"el valor total del producto con descuento es {i - (descuento * i)}")