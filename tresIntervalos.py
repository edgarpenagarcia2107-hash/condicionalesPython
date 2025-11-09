x = int(input("ingrese un numero -> "))
limite1 = int(input("ingrese el limite 1 -> "))
limite2 = int(input("ingrese el limite 2 -> "))
limite3 = int(input("ingrese el limite 3 -> "))
limite4 = int(input("ingrese el limite 4 -> "))
limite5 = int(input("ingrese el limite 5 -> "))
limite6 = int(input("ingrese el limite 6 -> "))

if x >= limite1 and x <= limite2:
    print("esta en el intervalo 1")
elif x >= limite3 and x <= limite4:
    print("esta en el intervalo 2")
elif x >= limite5 and x <= limite6:
    print("esta en el intervalo 3")
else:
    print("no esta en ningun intervalo")