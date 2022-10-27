class Empresa:

    def __init__(self, nombre):
        self.nombre = nombre
    
    def __str__(self):
        return "%s" %(self.nombre)
    
    def __repr__(self):
        return self.__str__()
    
    def __eq__(self, other) -> bool:
        return self.nombre == other.nombre