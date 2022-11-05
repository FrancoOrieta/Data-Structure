from unsorted_priority_queue_abstract import UnsortedPriorityQueueAbstract
from python_ed_fcad_uner.data_structures import PriorityQueueBase
from typing import Any, Tuple

class UnsortedPriorityQueue(UnsortedPriorityQueueAbstract):
    
    def __init__(self):
        self._element = []
        self._size = 0
    
    def add(self, k: Any, v: Any) -> None:
        queue = PriorityQueueBase()
        queue._key = k
        queue._value = v

        elemento = (queue._key, queue._value)
        self._element.append(elemento)
        self._size += 1

    def is_empty(self) -> bool:
        return self._size == 0

    def __str__(self) -> str:

        if self.is_empty():
            return "UnsortedPriorityQueue()"

        res = ""
        for i in range(0,len(self._element)):
            res += str(self._element[i]) + ","

        res = res[:-1]

        return f"UnsortedPriorityQueue({res})"
    
    def __len__(self) -> int:
        return self._size

    def min(self) -> Tuple[Any]:

        if self.is_empty():
            raise Exception("Operación no soportada, la estructura está vacía.")
        
        min_elemento = self._element[0]

        for i in range(0,len(self._element)):

            if min_elemento[0] > self._element[i][0]:
                min_elemento = self._element[i]
        
        return min_elemento
    
    def remove_min(self) -> Tuple[Any]:

        if self.is_empty():
            raise Exception("Operación no soportada, la estructura está vacía.")

        min_elemento = self.min()

        indice = self._element.index(min_elemento)
        
        min_remove = self._element.pop(indice)
        self._size -= 1 
        return min_remove