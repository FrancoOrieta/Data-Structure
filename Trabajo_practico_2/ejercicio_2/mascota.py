from raza import Raza
from persona import Persona

class Mascota:
    ANIO_ACTUAL = 2022

    def __init__(self, num_registro, nombre, raza : Raza, anio_nacimiento, dueño : Persona):
        self.__num_registro = num_registro
        self.__nombre = nombre
        self.__raza = raza
        self.__anio_nacimiento = anio_nacimiento
        self.__dueño = dueño
    
    def __str__(self):
        return "* Numero de registro: %d\n* Nombre de la mascota: %s\n* Raza: %s\n* Año de nacimiento: %d\n%s" %(self.__num_registro, self.__nombre, self.__raza, self.__anio_nacimiento, self.__dueño)
    
    def __repr__(self):
        return self.__str__()

    def __eq__(self, other): 
        return self.__raza == other.__raza and self.__num_registro == other.__num_registro
    
    @property
    def nombre(self):
        return self.__nombre

    @property
    def num_registro(self):
        return self.__num_registro

    @property
    def anio_nacimiento(self):
        return self.__anio_nacimiento

    @property
    def dueño(self):
        return self.__dueño
    
    @property
    def raza(self):
        return self.__raza
    
    @property
    def edad(self):
        return abs(self.ANIO_ACTUAL - self.__anio_nacimiento)

    @edad.setter
    def edad(self, edad):
        raise Exception("No se puede modificar la edad")