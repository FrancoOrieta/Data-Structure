from data_structures import LinkedStack
from typing import List, Any
from linked_stack_ext_abs import LinkedStackExtAbstract

class LinkedStackExt(LinkedStackExtAbstract, LinkedStack):
    
    def multi_pop(self, num: int) -> List[Any]:
        lista = []
        if not self.is_empty():
            for i in range(0, num):
                lista.append(self.pop())
        else:
            raise Exception("No es posible quitar elemento, pila vacia")
        return lista
    
    def replace_all(self, param1: Any, param2: Any) -> None:
        actual = self._head
        for i in range(0,self.__len__()):
            if actual.element == param1:
                actual.element = param2
                actual = actual.next
            else:
                actual = actual.next

    def exchange(self) -> None:
        tope = self._head
        reco = self._head
        if not self.is_empty():
            for i in range(0,self.__len__()):
                if reco.next == None:
                    tope.element, reco.element = reco.element, tope.element
                else:
                    reco = reco.next
        else:
            raise Exception("Operacion invalida, la pila esta vacia")