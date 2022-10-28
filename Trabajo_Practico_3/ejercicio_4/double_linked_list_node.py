from typing import Any, Union

class LinkedListNode:
    
    __slots__= "element", "next", "prev"

    def __init__(self, element : Any, next = None, prev = None) -> None:
        self.element = element
        self.next : Union[LinkedListNode, None] = next
        self.prev : Union[LinkedListNode, None] = prev