from typing import Any
from python_ed_fcad_uner.data_structures import PriorityQueueBase

class PriorityQueueStack():
    
    def __init__(self) -> None:
        self._data = []
        self._key = 1

    def push(self, elem: Any):
        queue = PriorityQueueBase()
        queue._key = self._key
        queue._value = elem

        self._key += 1

        if not self.is_empty():

            """ Acomoda las keys de modo que el ultimo elemento insertado tenga la mayor
            prioridad, es decir el valor de clave mas chico """

            for elemento in self._data:
                if elemento._key < self._key:
                    elemento._key, queue._key = queue._key, elemento._key

        self._data.append(queue)
    
    def __len__(self):
        return len(self._data)
    
    def is_empty(self):
        return len(self._data) == 0

    def __str__(self) -> str:

        if self.is_empty():
            return "PriorityQueueStack()"

        res = ""
        for elem in self._data[::-1]:
            res += "(key= " + str(elem._key) + ", elem= " + str(elem._value) + "), " 

        res = res[:len(res)-2]

        return f"PriorityQueueStack({res})"

    def pop(self):

        if self.is_empty():
            raise Exception("La pila está vacía")

        elem = self._data.pop()

        self._key = 1
        return elem._value
        
    def top(self):

        if self.is_empty():
            raise Exception("No hay tope, pila vacia")
        
        tope = self._data[len(self._data)-1]

        return tope._value