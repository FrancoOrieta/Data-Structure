from math import pi

print("Calcular el perimetro de un circulo".center(50,"*"))
radio = float(input("Ingresar el radio de un circulo: "))

while radio < 0:
    print("El radio no puede ser negativo")
    radio = float(input("Ingresar el radio de un circulo: "))

diametro = radio*2

print("pi*radio*2 = ",pi*radio*2)

print("diametro*pi = ", pi*diametro)
