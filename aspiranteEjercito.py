sexo = input("Ingrese el sexo del aspirante (M para mujer, H para hombre): ")
edad = int(input("Ingrese la edad del aspirante: "))
estatura = float(input("Ingrese la estatura del aspirante en metros: "))
estado_civil = input("¿Es soltero/a? (S/N): ")

apto = False

if estado_civil == "S":
    if sexo == "M" and estatura > 1.60 and 20 <= edad <= 25:
        apto = True
    elif sexo == "H" and estatura > 1.65 and 18 <= edad <= 24:
        apto = True

if apto:
    print("El aspirante ES APTO para ingresar al ejército.")
else:
    print("El aspirante NO ES APTO para ingresar al ejército.")