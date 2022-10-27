from typing import List, Any
from linked_binary_tree_ext_abstract import LinkedBinaryTreeExtAbstract
from python_ed_fcad_uner.data_structures import LinkedBinaryTree
from python_ed_fcad_uner.data_structures import BinaryTreeNode
from python_ed_fcad_uner.data_structures import LinkedQueue

class LinkedBinaryTreeExt(LinkedBinaryTreeExtAbstract, LinkedBinaryTree):

    def hermanos(self, nodo1: BinaryTreeNode, nodo2: BinaryTreeNode) -> bool:
        cola = LinkedQueue()
        cola.enqueue(self._root)

        if nodo1 == self._root or nodo2 == self._root:
            return False

        while not cola.is_empty():

            actual = cola.first()

            if actual.left_child:
                cola.enqueue(actual.left_child)

                if actual.left_child == nodo1 or actual.left_child == nodo2:
                    padre1 = actual

                if actual.right_child:
                    cola.enqueue(actual.right_child)     

                    if actual.right_child == nodo1 or actual.right_child == nodo2:
                        padre2 = actual

            cola.dequeue()

        return padre1 == padre2

    def hojas(self) -> List[Any]:
        lista_hojas = []

        cola = LinkedQueue()
        cola.enqueue(self._root)

        while not cola.is_empty():
            actual = cola.first()

            if actual.left_child:
                cola.enqueue(actual.left_child)

                if actual.right_child:
                    cola.enqueue(actual.right_child)

                cola.dequeue()
            else:
                lista_hojas.append(actual)
                cola.dequeue()

        return lista_hojas
    
    def internos(self) -> List[Any]:
        lista_internos = []

        cola = LinkedQueue()
        cola.enqueue(self._root)

        while not cola.is_empty():
            actual = cola.first()

            if actual.left_child:
                hijo_izq = actual.left_child

                if hijo_izq.left_child:
                    lista_internos.append(hijo_izq)
                    cola.enqueue(actual.left_child)

                if actual.right_child:
                    hijo_der = actual.right_child

                    if hijo_der.left_child:
                        lista_internos.append(hijo_der)
                        cola.enqueue(actual.right_child)

                cola.dequeue()

        return lista_internos
    
    def profundidad(self, nodo: BinaryTreeNode) -> int:

        cola = LinkedQueue()
        cola.enqueue(self._root)

        if nodo == self._root:
            return 0

        profundidad = 1
        while not cola.is_empty():
            actual = cola.first()

            if not actual.left_child:
                profundidad = 1

            if actual.left_child == nodo or actual.right_child == nodo:
                return profundidad
            else:
                cola.enqueue(actual.left_child)
                cola.enqueue(actual.right_child)

            profundidad += 1
            cola.dequeue()

          
    def altura(self, nodo: BinaryTreeNode) -> int:

        cola_izq = LinkedQueue()
        cola_izq.enqueue(nodo)
        altura_izq = 0

        cola_der = LinkedQueue()
        cola_der.enqueue(nodo)
        altura_der = 0

        while not cola_izq.is_empty():
            
            actual_izq = cola_izq.first()
            if actual_izq.left_child:
                cola_izq.enqueue(actual_izq.left_child)
                altura_izq += 1
            cola_izq.dequeue()
            
        while not cola_der.is_empty():
            actual_der = cola_der.first()
            if actual_der.right_child:
                cola_der.enqueue(actual_der.right_child)
                altura_der += 1
            cola_der.dequeue()
            
        if altura_der > altura_izq:
            return altura_der

        elif altura_izq > altura_der:
            return altura_izq

        else:
            return altura_izq