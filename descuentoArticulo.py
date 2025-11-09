i = int(input("ingrese el tipo de su producto "))
j = float(input("ingrese el valor de su producto "))


if i == 1:
    descuento = j * 0.125
elif i == 2:
    descuento = j * 0.083
elif i == 3:
    descuento = j * 0.032
else:
    descuento = j * 0.0

print(f"el valor del descuento del producto es -> {descuento}$")
print(f"el valor total a pagar es de -> {j - descuento}")
