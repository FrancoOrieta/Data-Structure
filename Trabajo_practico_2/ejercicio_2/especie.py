class Especie:

    def __init__(self, nombre):
        self.__nombre = nombre
    
    def __str__(self):
        return "%s" %(self.__nombre)
        
    def __repr__(self):
        return self.__str__()
        
    def __eq__(self, other):
        return self.__nombre == other.__nombre
       
    @property
    def nombre(self):
        return self.__nombre