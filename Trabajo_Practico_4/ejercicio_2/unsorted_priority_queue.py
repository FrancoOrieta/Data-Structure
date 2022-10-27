from unsorted_priority_queue_abstract import UnsortedPriorityQueueAbstract
from typing import Any

class UnsortedPriorityQueue(UnsortedPriorityQueueAbstract):
    
    def __init__(self):
        self._element = []
        self._size = 0
    
    def add(self, k: Any, v: Any) -> None:
        elemento = (k,v)
        self._element.append(elemento)
        self._size += 1

    def is_empty(self) -> bool:
        return self._size == 0

    def __str__(self) -> str:

        if self.is_empty():
            return "UnsortedPriorityQueue()"

        res = ""
        for i in range(0,self._element.__len__()):
            res += str(self._element[i]) + ","

        res = res[:-1]

        return f"UnsortedPriorityQueue({res})"
    
    def __len__(self) -> int:
        return self._size