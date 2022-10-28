from unsorted_priority_queue_abstract import UnsortedPriorityQueueAbstract
from python_ed_fcad_uner.data_structures import PriorityQueueBase
from typing import Any, Tuple

class UnsortedPriorityQueue(UnsortedPriorityQueueAbstract):
    
    def __init__(self):
        self._element = []
        self._size = 0
    
    def add(self, k: Any, v: Any) -> None:
        queue = PriorityQueueBase()
        queue._Item._key = k
        queue._Item._value = v

        elemento = (queue._Item._key, queue._Item._value)
        self._element.append(elemento)
        self._size += 1

    def is_empty(self) -> bool:
        return self._size == 0

    def __str__(self) -> str:

        if self.is_empty():
            return "UnsortedPriorityQueue()"

        res = ""
        for i in range(0,len(self._element)):
            res += str(self._element[i]) + ","

        res = res[:-1]

        return f"UnsortedPriorityQueue({res})"
    
    def __len__(self) -> int:
        return self._size

    def min(self) -> Tuple[Any]:

        if self.is_empty():
            raise Exception("Operación no soportada, la estructura está vacía.")
        
        #min_elemento: la usamos como variable de busqueda
        #Toma el valor de la primer tupla de la lista
        min_elemento = self._element[0]

        #Recorremos toda la lista
        for i in range(0,len(self._element)):

            #min_elemento[0]: Hacemos referencia a la k en la tupla
            #self_element[i][0]: Con [i] referenciamos una tupla de la lista y con [0] referenciamos la k de la tupla
            #True: significa que aun no hayamos el min_valor, cambiamos min_elemento por la tupla [i] de la lista
            if min_elemento[0] > self._element[i][0]:
                min_elemento = self._element[i]
        
        return min_elemento #retornamos la tupla con menor clave
    
    def remove_min(self) -> Tuple[Any]:

        if self.is_empty():
            raise Exception("Operación no soportada, la estructura está vacía.")
        
        #llamamos a la funcion min para obtener el minimo elemento
        min_elemento = self.min()

        #la funcion de lista (lista.index(A)): retorna el indice del elemento A en la lista
        #guardamos el indice del elemento con menor clave
        indice = self._element.index(min_elemento)
        
        min_remove = self._element.pop(indice) #Eliminamos el elemento minimo y lo retornamos
        self._size -= 1     #Decrece el tamaño de la cola
        return min_remove