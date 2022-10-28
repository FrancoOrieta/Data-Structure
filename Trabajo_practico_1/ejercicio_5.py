from funciones import jugar, generar_random

lim_1 = int(input("Ingrese un limite\n"))
lim_2 = int(input("Ingrese otro limite\n"))

numero_random = generar_random(lim_1,lim_2)

if lim_1 < lim_2:
    print("Estoy pensando en un numero entre " + str(lim_1) + " y " + str(lim_2) + "\n")
else:
    print("Estoy pensando en un numero entre " + str(lim_2) + " y " + str(lim_1) + "\n")

num_jugador = int(input("Adivina el numero\n"))

jugar(num_jugador, numero_random)