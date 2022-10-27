from oficina import Oficina

class Empleado:

    def __init__(self, legajo, dni, apellido, nombre, oficina : Oficina):
        self.legajo = legajo
        self.dni = dni
        self.apellido = apellido
        self.nombre = nombre
        self.oficina = oficina
    
    def __str__(self):
        return "* Empleado %s, %s\n   Legajo: %d\n   DNI: %d\n* Oficina en el %s" %(self.apellido, self.nombre, self.legajo, self.dni, self.oficina)
    
    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.legajo == other.legajo
    
    def __lt__(self, other):
        return self.legajo < other.legajo

    def __hash__(self):
        return id(self)