from typing import Any, Union, Iterator
from double_linked_list_abstract import DoubleLinkedListAbstract
from double_linked_list_node import LinkedListNode

class DoubleLinkedList(DoubleLinkedListAbstract):

    def __init__(self) -> None:
        self._header: LinkedListNode = LinkedListNode(None, None, None)
        self._size: int = 0

    def __len__(self) -> int:
        return self._size
    
    def __getitem__(self, key: int) -> Union[Any, None]:
        if self.is_empty():
            raise Exception("Operación no permitida si la estructura está vacía.")

        if key < 0 or key >= self._size:
            raise Exception("Índice fuera de rango. No se puede continuar.")

        i = 0
        actual = self._header.next
        while actual:
            if i == key:
                return actual.element
            actual = actual.next
            i += 1

        return None

    def __setitem__(self, key: int, value: Any) -> None:
        if self.is_empty():
            raise Exception("Operación no permitida si la estructura está vacía.")

        if key < 0 or key >= self._size:
            raise Exception("Índice fuera de rango. No se puede continuar.")

        i = 0 
        
        actual = self._header.next
        
        while actual:
            if i == key:
                actual.element = value
            actual = actual.next
            i += 1
    
    def __delitem__(self, key: int) -> None:
        if self.is_empty():
            raise Exception("Operación no permitida si la estructura está vacía.")

        if key < 0 or key >= self._size:
            raise Exception("Índice fuera de rango. No se puede continuar.")

        i = 0

        previo = self._header.prev
        actual = self._header.next
        while actual:
            if i == key:
                break
            previo = actual
            actual = actual.next
            i += 1

        if previo: 
            previo.next = actual.next
        else:
            self._header.next = actual.next

        self._size -= 1

    def __iter__(self) -> Iterator[Any]:
        actual = self._header.next

        for i in range(0, self.__len__()):
            yield actual.element
            actual = actual.next
            
    def __str__(self) -> str:
        if self.is_empty():
            return "DoubleLinkedList()"
        
        res = ""
        actual = self._header.next

        while actual:
            res += str(actual.element) + ", "
            actual = actual.next

        res = res[:-2]

        return f"DoubleLinkedList({res})"

    def is_empty(self) -> bool:
        return self._size == 0

    def append(self, elem: Any) -> None:
        nuevo_nodo = LinkedListNode(elem)
        if self.is_empty():
            self._header.next = nuevo_nodo
        else:
            actual = self._header

            while actual.next:
                actual = actual.next
            actual.next = nuevo_nodo
            nuevo_nodo.prev = actual

        self._size += 1