from funciones import ingresar_Ciudades, imprimir_Ciudades

print("Ingrese el nombre de tres ciudades, una a la vez")
a = input()
b = input()
c = input()

ciudades = [a, b, c]

respuesta = input("¿Desea añadir más ciudades a la lista?\n")

ciudades = ingresar_Ciudades(respuesta, ciudades)
imprimir_Ciudades(ciudades)