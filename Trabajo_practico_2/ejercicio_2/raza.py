from especie import Especie

class Raza:

    def __init__(self, nombre, especie : Especie):
        self.__nombre = nombre
        self.__especie = especie

    def __str__(self):
        return "%s - %s" %(self.__nombre, self.__especie)

    def __repr__(self):
        return self.__str__()
        
    def __eq__(self, other):
        return self.__especie == other.__especie

    @property
    def nombre(self):
        return self.__nombre

    @property
    def especie(self):
        return self.__especie