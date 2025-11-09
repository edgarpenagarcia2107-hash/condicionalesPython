import math
a = int(input("ingrese el valor de a "))
b = int(input("ingrese el valor de b "))
c = int(input("ingrese el valor de c "))

if  (b**2 -4*a*c) >= 0 and a != 0:
    print("la ecuacion tiene dos soluciones")
else:
    print("la ecuacion no tiene soluciones")
    