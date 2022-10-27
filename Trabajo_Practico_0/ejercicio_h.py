a = int(input("Ingrese un primer número\n"))
b = int(input("Ingrese un segundo número\n"))
c = int(input("Ingrese un tercer número\n"))

print(" ")

if a > b:
    if b > c:
        print("El mayor numero de los tres es " + str(a))
    elif c > a:
        print("El mayor numero de los tres es " + str(c))
    else:
        print("El mayor numero de los tres es " + str(a))
else:
    if a > c:
        print("El mayor numero de los tres es " + str(b))
    elif c > b:
        print("El mayor numero de los tres es " + str(c))
    else:
        print("El mayor numero de los tres es " + str(b))