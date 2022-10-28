class Categoria:

    def __init__(self, nombre, *args):
        self.__nombre = nombre
        self.__args = args

    @property
    def nombre(self):
        return self.__nombre
    
    def __str__(self):
        return "%s\n* Subcategoría: %r" % (self.__nombre, self.__args)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.__nombre == other.__nombre