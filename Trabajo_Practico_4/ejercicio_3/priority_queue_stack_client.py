from priority_queue_stack import PriorityQueueStack

stack = PriorityQueueStack()

print("Llenando la pila".center(36, "*"))
print("Cargando...\n")
stack.push(20)
stack.push(4)
stack.push(81)
stack.push(55)
stack.push(2)
stack.push(18)
stack.push(11)
stack.push(40)
stack.push(6)
stack.push(8)

print("Pila vacia?".center(26, "*"))
print(stack.is_empty(),"\n")

print("Longitud".center(26, "*"))
print(len(stack),"\n")

print("Pila".center(20, "*"))
print(stack,"\n")

print("Pop".center(20, "*"))
print("Elemento quitado: ", stack.pop())
print("Elemento quitado: ", stack.pop())
print("Elemento quitado: ", stack.pop(),"\n")

print("Pila despues del pop".center(35, "*"))
print(stack,"\n")

print("Tope".center(20, "*"))
print(stack.top())