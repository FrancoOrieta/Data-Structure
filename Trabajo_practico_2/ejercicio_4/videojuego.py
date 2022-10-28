import datetime
from plataforma import Plataforma
from genero import Genero
from empresa import Empresa

class Videojuego:

    def __init__(self, titulo, genero: Genero, plataforma: Plataforma, descripcion, precio: float, desarrolladora : Empresa, distribuidora : Empresa, fecha_lanzamiento : datetime, ranking):
        self.titulo = titulo
        self.genero = genero
        self.plataforma = plataforma
        self.descripcion = descripcion
        self.precio = precio
        self.desarrolladora = desarrolladora
        self.distribuidora = distribuidora
        self.fecha_lanzamiento = fecha_lanzamiento
        self.__ranking = ranking
    
    def __str__(self):
        return "* Titulo: %s\n* Genero: %s\n* Plataformas: %s\n* Descripción: %s\n* Precio en USD: %.2f\n* Desarrollado por %s\n* Distribución a cargo de %s\n* Fecha de lanzamiento: %s\n* Ranking: %.2f\n" %(self.titulo, self.genero, self.plataforma, self.descripcion, self.precio, self.desarrolladora, self.distribuidora, self.fecha_lanzamiento, self.ranking)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        if self.desarrolladora == other.desarrolladora and self.titulo == other.titulo:
            return True
        else: return False

    @property
    def ranking(self):
        return self.__ranking

    @ranking.setter
    def ranking(self, num):
        if num <= 10 and num >= 0:
            self.__ranking = num
        else:
            raise Exception(ValueError)