i = float(input("Ingrese su primer nota -> "))
j = float(input("Ingrese su segunda nota -> "))
k = float(input("Ingrese su tercer nota -> "))
l = float(input("Ingrese su cuarta nota -> "))
m = float(input("Ingrese su quinta nota -> "))
promedio = (i + j + k + l + m) / 5
print(f"Su promedio es {promedio}")
if promedio >= 3.5:
    print("Aprobado")
else:
    print("Reprobado")