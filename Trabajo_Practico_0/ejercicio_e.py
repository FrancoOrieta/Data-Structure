cuenta = float(input("¿Cúanto es el total por la cena? Ingrese el monto\n"))

while cuenta != 0:
    if cuenta >= 1:
        invitados = int(input("Ingrese la cantidad de invitados que comieron\n"))
        print(" ")
        
        importe_individual = str(cuenta/invitados)
        print("El importe a pagar por cabeza es de " + importe_individual)
    else:
        print("Valor de cuenta invalido")
        cuenta = float(input("Reingrese el monto o escriba 0 para salir\n"))
