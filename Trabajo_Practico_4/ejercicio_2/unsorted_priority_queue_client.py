from unsorted_priority_queue import UnsortedPriorityQueue

cola_prioridad = UnsortedPriorityQueue()

print("Llenando cola".center(36, "*"))
cola_prioridad.add(4,"Franco")
cola_prioridad.add(5,"Sofi")
cola_prioridad.add(15,"Luciano")
cola_prioridad.add(1,"Flor <3")
cola_prioridad.add(9,"Agus")
cola_prioridad.add(6,"Taiel")

print("Cola actual".center(36, "*"))
print(cola_prioridad,"\n")

print("Longitud".center(36, "*"))
print(len(cola_prioridad),"\n")

print("Valor minimo".center(36, "*"))
print(cola_prioridad.min(),"\n")

print("Remover el minimo".center(36, "*"))
print("Elemento removido: ",cola_prioridad.remove_min(),"\n")

print("Cola actual".center(36, "*"))
print(cola_prioridad,"\n")
