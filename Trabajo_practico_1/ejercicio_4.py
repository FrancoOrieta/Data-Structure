num = int(input("Ingresar un numero\n"))
while num != 0:
    if num >= 10 and num <= 20:
        print("Gracias!!")
        num = 0
    elif num < 10:
        print("Valor inferior")
        num = int(input("Reingrese el numero\n"))
    else:
        print("Valor superior")
        num = int(input("Reingrese el numero\n"))