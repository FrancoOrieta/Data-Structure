from funciones import buscar_en_lista
lista1 = ["360","250","100","888"]

for i in range(0, len(lista1)):
    print(lista1[i])

num = input("Ingresar un numero de la lista\n")

posicion = buscar_en_lista(num, lista1)

if posicion >= 0:
    print("El numero ingresado se encuentra en posición: " + str(posicion))
else:
    print("El valor ingresado no es parte de la lista")