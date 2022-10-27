from double_linked_list import DoubleLinkedList

def llenando(de_list):
    for i in range(1,16):
        de_list.append(i)

double_lista = DoubleLinkedList()

print("")
print("Llenando la lista del 1-15".center(36, "*"))
llenando(double_lista)
print("Cargando...\n")

print("Tamaño".center(16,"*"))
print(double_lista.__len__(),"\n")

print("Lista".center(15,"*"))
print(double_lista,"\n")

print("Obtener los elementos de la posicion 2 y 8".center(43,"*"))
print(double_lista.__getitem__(2))
print(double_lista.__getitem__(8),"\n")

print("Cambiar el elemento de posicion 7".center(43,"*"))
double_lista.__setitem__(7,300)
print("Lista despues del cambio: ", double_lista,"\n")

print("Borrar los elementos de posicion 1 y 4".center(50,"*"))
double_lista.__delitem__(1)
print("Lista despues de borrar el elemento 1: ", double_lista)
double_lista.__delitem__(4)
print("Lista despues de borrar el elemento 4: ", double_lista,"\n")

print("Iterador".center(18,"*"))
for i in double_lista.__iter__():
    print(i)