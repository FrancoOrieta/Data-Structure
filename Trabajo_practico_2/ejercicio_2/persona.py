class Persona:

    def __init__(self, apellido, nombre, dni):
        self.__apellido = apellido
        self.__nombre = nombre
        self.__dni = dni

    def __str__(self):
        return "* Dueño: %s, %s\n* Documento: %d" %(self.__apellido, self.__nombre, self.__dni)

    def __repr__(self):
        return self.__str__()
    
    def __eq__(self, other):
        return self.__dni == other.__dni
   
    
    @property
    def dni(self):
        return self.__dni
    
    @property
    def apellido(self):
        return self.__apellido

    @property
    def nombre(self):
        return self.__nombre