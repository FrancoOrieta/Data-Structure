from typing import Any
from python_ed_fcad_uner.data_structures import PriorityQueueBase

class PriorityQueueStack(PriorityQueueBase):

    KEY = 10 #variable de clase para la key
    
    @classmethod
    def increment_key(cls):
        cls.KEY += 1

    @classmethod
    def decrement_key(cls):
        cls.KEY -= 1

    def __init__(self) -> None:
        super().__init__()
        self._data = []

    def push(self, elem: Any):

        self._key = self.KEY
        self._value = elem

        self._data.append((self._key, self._value))

        self.decrement_key()
    
    def __len__(self):
        return len(self._data)
    
    def is_empty(self):
        return len(self._data) == 0

    def __str__(self) -> str:

        if self.is_empty():
            return "PriorityQueueStack()"

        res = ""
        for elem in self._data[::-1]:
            res += str(elem[0]) + ", " #Retorna elem[0] la key, elem[1] retorna el valor

        res = res[:-2]

        return f"PriorityQueueStack({res})"

    def pop(self):

        if self.is_empty():
            raise Exception("La pila está vacía")

        elem = self._data.pop()
        self.increment_key()
        
        return elem[1]
        
    def top(self):

        if self.is_empty():
            raise Exception("No hay tope, pila vacia")

        return self._data[::-1][0][1]