from videojuegosAdminAbstracta import VideojuegosAdminAbstract
from videojuego import Videojuego
from empresa import Empresa
from genero import Genero

class videojuegosAdmin(VideojuegosAdminAbstract):

    def __str__(self) -> str:
        res = ""
        for elem in self.videojuegos:
            res += "{elem}\n".format(elem=str(elem))
        return res
    
    def agregar(self, videojuego: Videojuego) -> None:
        self.videojuegos.append(videojuego)
    
    def filtrar_por_desarrolladora(self, desarrolladora: Empresa) -> list:
        lista = []
        for video in self.videojuegos:
            if video.desarrolladora == desarrolladora:
                lista.append(video)
        return lista
    
    def filtrar_por_distribuidora(self, distribuidora: Empresa) -> list:
        lista = []
        for video in self.videojuegos:
            if video.distribuidora == distribuidora:
                lista.append(video)
        return lista
    
    def filtrar_por_genero(self, genero: Genero) -> list:
        lista = []
        for video in self.videojuegos:
            if video.genero == genero:
                lista.append(video)
        return lista

    def cantidad_por_plataforma(self) -> list:
        diccionario = {}
        lista = []
        for video in self.videojuegos:
            for plat in video.plataforma:
                key, valor = plat.nombre, 0
                diccionario[key] = valor

        for video in self.videojuegos:
            for plat in video.plataforma:
                if plat.nombre in diccionario:
                    diccionario[plat.nombre] += 1
        lista.append(diccionario)
        return lista

    def ordenar_titulo(self) -> None:
        self.videojuegos = sorted(self.videojuegos, key = lambda obj: (obj.titulo))
    
    def ordenar_mejores_primero(self) -> None:
        self.videojuegos = sorted(self.videojuegos, key = lambda obj: (obj.ranking), reverse = True)