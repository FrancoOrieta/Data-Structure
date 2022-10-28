class Plataforma:

    def __init__(self, nombre, es_portatil : bool):
        self.nombre = nombre
        self.es_portatil = es_portatil
    
    def __str__(self):
        return "%s - Portatil: %s" %(self.nombre, self.es_portatil)
    
    def __repr__(self) -> str:
        return self.__str__()