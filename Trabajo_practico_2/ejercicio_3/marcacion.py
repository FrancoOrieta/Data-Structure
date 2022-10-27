from datetime import datetime
from empleado import Empleado
from marcacionTipo import MarcacionTipo


class Marcacion:
    
    NUMERO_DE_REGISTROS = 0

    def __init__(self, empleado : Empleado, fecha_hora : datetime , tipo : MarcacionTipo):
        self.__num_registro = self.numeros_de_registro()
        self.empleado = empleado
        self.fecha_hora = fecha_hora
        self.tipo = tipo
    
    def __str__(self):
        return "* Numero registro: %d\n%s\n* Fecha y hora: %s\n* Tipo: %s"%(self.num_registro, self.empleado, self.fecha_hora, self.tipo)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.__num_registro == other.__num_registro

    @classmethod
    def numeros_de_registro(cls):
        cls.NUMERO_DE_REGISTROS += 1
        return cls.NUMERO_DE_REGISTROS
    
    @property
    def num_registro(self):
        return self.__num_registro

    @num_registro.setter
    def num_registro(self):
        raise Exception("El atributo numero de registro no se puede modificar")