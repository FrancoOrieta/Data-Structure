
canti_dias = input("Ingrese una cantidad de dias\n")

print(" ")

while int(canti_dias) != 0:
    if int(canti_dias) >= 1:
      horas = int(canti_dias)*24
      minutos = horas*60
      segundos = minutos*60

      print("En " + canti_dias + " dias hay " +
            str(horas) + " horas, " + str(minutos) + " minutos " +
             "y " + str(segundos) + " segundos")

      print(" ")
      
      canti_dias = input("Ingrese una nueva cantidad o ingrese 0 para salir\n")
    else:
      print("Cantidad de dias invalida")
      canti_dias = input("Ingrese una nueva cantidad o ingrese 0 para salir\n")
    