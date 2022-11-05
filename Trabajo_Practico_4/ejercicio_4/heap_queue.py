from typing import Any
from python_ed_fcad_uner.data_structures import ArrayHeap

class HeapQueue():

    def __init__(self):
        self._data = ArrayHeap()
        self._key = 1
    
    def is_empty(self):
        return self._data == 0
    
    def __len__(self):
        return len(self._data)

    def enqueue(self, elem: Any):
        self._data.add(self._key, elem)
        self._key += 1

    def dequeue(self):
        min = self._data.remove_min()
        return min

    def first(self):
        return self._data.min()