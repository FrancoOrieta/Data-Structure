from priority_queue_stack import PriorityQueueStack

stack = PriorityQueueStack()

def llenado(pila):
    for i in range(1,11):
        pila.push(i)

stack = PriorityQueueStack()

print("Llenando la pila".center(36, "*"))
print("Cargando...\n")
llenado(stack)

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