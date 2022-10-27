from typing import Any, Union

class DequeueListNode:
    
    __slots__ = "element", "next"
    
    def __init__(self, element : Any, next = None) -> None:
        self.element = element
        self.next : Union[DequeueListNode, None] = next