print("Ingrese sus cuatro platos favoritos, uno a la vez")
p1 = input()
p2 = input()
p3 = input()
p4 = input()

platos = {1:p1, 2:p2, 3:p3, 4:p4}

print(platos)

print("¿Qué comida desea quitar?")
c = int(input())

del platos[c]
print(platos)