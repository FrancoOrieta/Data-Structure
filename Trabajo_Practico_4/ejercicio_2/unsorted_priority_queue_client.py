from unsorted_priority_queue import UnsortedPriorityQueue

cola_prioridad = UnsortedPriorityQueue()

print("Llenando cola".center(26, "*"))
cola_prioridad.add(4,"Franco")
cola_prioridad.add(5,"Sofi")
cola_prioridad.add(15,"Luciano")
cola_prioridad.add(1,"Flor")
cola_prioridad.add(9,"Agus")
cola_prioridad.add(6,"Taiel")
print("")

print("Cola actual".center(26, "*"))
print(cola_prioridad,"\n")

print("Longitud".center(26, "*"))
print(len(cola_prioridad),"\n")

print("Valor minimo".center(26, "*"))
print(cola_prioridad.min(),"\n")

print("Remover el minimo".center(26, "*"))
print("Elemento removido: ",cola_prioridad.remove_min(),"\n")

print("Cola actual".center(26, "*"))
print(cola_prioridad,"\n")
