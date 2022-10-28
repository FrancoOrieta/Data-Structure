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