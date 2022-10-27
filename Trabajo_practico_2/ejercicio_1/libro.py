from autor import Autor
from categoria import Categoria

class Libro:

    def __init__ (self, num_inventario, titulo, autor : Autor, categoria : Categoria, anio_de_publicación):
        self.__num_inventario = num_inventario
        self.__titulo = titulo
        self.__Autor = autor
        self.__categoria = categoria
        self.__anio_de_publicación = anio_de_publicación
    
    @property
    def num_inventario(self):
        return self.__num_inventario

    @property
    def titulo(self):
        return self.__titulo

    @property
    def Autor(self):
        return self.__Autor

    @property
    def categoria(self):
        return self.__categoria
    
    @property
    def anio_de_publicación(self):
        return self.__anio_de_publicación
    
    def __str__(self):
        return "* Numero de Inventario: %d\n* Titulo: %s\n* Autor: %s\n* Categoría: %s\n* Año de Publicación: %d" % (self.__num_inventario, self.__titulo, self.__Autor, self.__categoria, self.__anio_de_publicación)
    
    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.__num_inventario == other.__num_inventario 