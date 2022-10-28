from datetime import datetime

class Oficina:
    
    def __init__(self, nombre,  hora_entrada : datetime.time,  hora_salida : datetime.time):
        self.nombre = nombre
        self.hora_entrada = hora_entrada
        self.hora_salida = hora_salida
    
    def __str__(self):
        return "sector de %s\n   Hora de entrada: %s\n   Hora de salida: %s" %(self.nombre, self.hora_entrada, self.hora_salida)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.nombre == other.nombre