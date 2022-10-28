start = input("Ingrese la forma de conteo deseada, ascendente o descendente\n")

if start == "ascendente" or start == "Ascendente" or start == "ASCENDENTE" or start == "asc" or start == "Asc" or start == "ASC":
    num = int(input("Ingrese un limite superior\n"))
    for i in range(1, num):
        print(i)

elif start == "descendente" or start == "Descendente" or start == "DESCENDENTE" or start == "des" or start == "Des" or start == "DES":
    num = int(input("Ingrese un limite inferior\n"))
    if num < 20:
        for i in range(20, num,-1):
            print(i)
    else:
        print("Número fuera del limite superior")

else:
    print("Incorrecto no se puede continuar")
