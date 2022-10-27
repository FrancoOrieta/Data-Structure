base = int(input("Ingrese la base de un triangulo: "))
while base < 0:
    print("La base no puede ser negativa")
    base = int(input("Ingrese la base de un triangulo: "))

altura = int(input("Ingrese la altura de un triangulo: "))
while altura < 0:
    print("La base no puede ser negativa")
    altura = int(input("Ingrese la altura de un triangulo: "))

print("Calculando la superficie de un triangulo".center(50,"*"))
print((base*altura)/2)
