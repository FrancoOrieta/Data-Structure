from linked_stack_ext import LinkedStackExt

pila = LinkedStackExt()

def pushing_numbers(stack):
    for i in range(1,11):
        stack.push(i)
        if i%2 == 0:     #Pushea tres veces mas los numeros pares, unicamente para que haya elementos repetidos
            stack.push(i)
            stack.push(i)
            stack.push(i)
print("")

print("Llenado de pila del 1-10".center(36, "*"))
pushing_numbers(pila)
print("Filling...\n")

print("Imprime Pila".center(22, "*"))
print(pila,"\n")

print("Longitud".center(18, "*"))
print(pila.__len__(),"\n")

print("MultiPop".center(18, "*"))
print(pila.multi_pop(6))
print("Pila luego del pop: ",pila,"\n")

print("Remplazo".center(18, "*"))
pila.replace_all(2,18)
print(pila,"\n")

print("Exchange".center(18, "*"))
pila.exchange()
print(pila,"\n")