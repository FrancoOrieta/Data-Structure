class Autor:

    def __init__(self, apellido, nombre):
        self.__apellido = apellido
        self.__nombre = nombre
    
    @property
    def apellido(self):
        return self.__apellido

    @property
    def nombre(self):
        return self.__nombre

    def __str__(self):
        return "%s, %s" % (self.__apellido, self.__nombre)
    
    def __repr__(self):
        return self.__str__()
    
    def __eq__(self, other):
        return self.__apellido == other.__apellido and self.__nombre == other.__nombre