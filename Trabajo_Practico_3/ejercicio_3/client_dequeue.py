from dequeue import DoubleQueue

def llenando(queue):
    for i in range(1,11):
        queue.add_first(i)

cola = DoubleQueue()
print("\n")

print("Llenando la cola por orden de llegada (1-10)".center(54,"*"))
print("Loading...\n")
llenando(cola)

print("Tamaño".center(16,"*"))
print(cola.__len__(),"\n")

print("Cola".center(14,"*"))
print(cola,"\n")

print("Primero de la cola".center(28,"*"))
print(cola.first(),"\n")

print("Ultimo de la cola".center(27,"*"))
print(cola.last(),"\n")

# print("Añade tres numeros al principio".center(41,"*"))
# cola.add_first(15)
# cola.add_first(20)
# cola.add_first(25)
# print(cola,"\n")

# print("Añade tres numeros al final".center(37,"*"))
# cola.add_last(222)
# cola.add_last(255)
# cola.add_last(500)
# print(cola,"\n")

print("Borra el primero de la cola".center(37,"*"))
cola.delete_first()
print(cola,"\n")

print("Borra el ultimo de la cola".center(36,"*"))
cola.delete_last()
print(cola,"\n")