from typing import Any
from python_ed_fcad_uner.data_structures import ArrayHeap

class HeapQueue(ArrayHeap):

    KEY = 1

    @classmethod
    def increment_key(cls):
        cls.KEY += 1
    
    @classmethod
    def decrecrement_key(cls):
        cls.KEY -= 1

    def enqueue(self, elem: Any):
        self.add(self.KEY, elem)
        self.increment_key()

    def dequeue(self):
        min = self.remove_min()[1]
        self.decrecrement_key()
        return min

    def first(self):
        return self.min()