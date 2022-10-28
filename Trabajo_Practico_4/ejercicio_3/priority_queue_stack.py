from typing import Any
from unsorted_priority_queue import UnsortedPriorityQueue

class PriorityQueueStack(UnsortedPriorityQueue):

    KEY = 1 #variable de clase para la key

    def __str__(self) -> str:

        if self.is_empty():
            return "PriorityQueueStack()"

        res = ""
        for elem in self._element[::-1]:
            res += str(elem[1]) + ", "

        res = res[:-2]

        return f"PriorityQueueStack({res})"
    
    @classmethod
    def increment_key(cls):
        cls.KEY += 1

    def push(self, elem: Any):
        self.add(self.KEY ,elem)
        self.increment_key()
    
    @classmethod
    def decrement_key(cls):
        cls.KEY -= 1

    def pop(self):

        if self.is_empty():
            raise Exception("La pila está vacía")

        elem = self._element.pop()
        self._size -= 1
        self.decrement_key()
        
        return elem[1]
        
    def top(self):

        if self.is_empty():
            raise Exception("No hay tope, pila vacia")

        return self._element[::-1][0][1]