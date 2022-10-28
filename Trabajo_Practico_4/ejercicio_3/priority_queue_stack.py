from unsorted_priority_queue import UnsortedPriorityQueue

class PriorityQueueStack(UnsortedPriorityQueue):


    def __init__(self):
        self._element = []
        self._size = 0
    
    def __len__(self):
        return self._size