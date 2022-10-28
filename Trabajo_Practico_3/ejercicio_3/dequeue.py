from typing import Any, Union
from dequeue_list_node import DequeueListNode
from dequeue_abstract import DequeAbstract


class DoubleQueue(DequeAbstract):

    def __init__(self):
        self._front: Union[DequeueListNode, None] = None
        self._back: Union[DequeueListNode, None] = None
        self._size : int = 0
    
    def __len__(self) -> int:
        return self._size
    
    def __str__(self) -> str:
        
        if self.is_empty():
            return ("DoubleQueue()")
        
        resultado = ""

        actual = self._front
        while actual != None:
            resultado += str(actual.element) + ", "
            
            actual = actual.next 
          
        resultado = resultado[:len(resultado)-2]
        
        return f"DoubleQueue({resultado})"
    
    def is_empty(self) -> bool:
        return self._size == 0

    def first(self) -> Any:
        if not self.is_empty():
            return self._front.element
        else:
            raise Exception("Operacion no realizada, coleccion vacia")
    
    def last(self) -> Any:
        if not self.is_empty():
            return self._back.element
        else:
            raise Exception("Operacion no realizada, coleccion vacia")
    
    def add_first(self, element: Any) -> None:

        nuevo_nodo = DequeueListNode(element, None)
        
        if self.is_empty():
            self._front = nuevo_nodo
            self._back = nuevo_nodo
        else:
            nuevo_nodo.next = self._front
            self._front = nuevo_nodo

        self._size += 1
    
    def add_last(self, element: Any) -> None:
        
        nuevo_nodo = DequeueListNode(element, None)
        
        if self.is_empty():
            self._front = nuevo_nodo
            self._back = nuevo_nodo
        else:
            self._back.next = nuevo_nodo
            self._back = self._back.next
            
        self._size += 1
    
    def delete_first(self) -> None:

        if self.is_empty():
            raise Exception("Estructura vacía. No se puede continuar")
        
        self._front = self._front.next
        self._size -= 1
    
    def delete_last(self) -> None:

        if self.is_empty():
            raise Exception("Estructura vacía. No se puede continuar")
        
        buscador = self._front

        for i in range(0,self.__len__()-1):
            if buscador.next.element == self._back.element:
                buscador.next = None
                self._back = buscador
            else:
                buscador = buscador.next
        self._size -= 1