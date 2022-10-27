num = int(input("Ingresar un número entero \n"))

if num > 1 and num < 12:
    for i in range(1,11):
        print(str(num) + " * " + str(i) + " = " + str(num*i))
         
elif num <= 1:
    print("El número ingresado debe ser mayor a 1")
else:
    print("El número ingresado debe ser menor a 12")