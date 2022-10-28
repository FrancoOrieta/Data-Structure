colores = ["Azul", "Verde", "Rojo", "Amarillo", "Violeta", "Rosa",
"Negro", "Celeste", "Gris", "Blanco"]

num_ini = int(input("Ingresar un numero de inicio, rango valido entre 0 y 4\n"))
num_fin = int(input("Ingresar un numero de fin, rango valido entre 5 y 9\n"))

nueva_lista = colores[num_ini:num_fin]
print(nueva_lista)