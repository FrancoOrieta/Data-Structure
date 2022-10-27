cadena = input("Ingresar una cadena\n")
i = len(cadena) - 1

nueva_cad = ""
while i >= 0:
    nueva_cad += cadena[i]
    i -= 1
print(nueva_cad)