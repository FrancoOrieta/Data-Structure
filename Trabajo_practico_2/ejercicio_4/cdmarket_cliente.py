import datetime
from videojuegosAdmin import videojuegosAdmin
from empresa import Empresa
from genero import Genero
from videojuego import Videojuego
from plataforma import Plataforma


def imprimir(lista):
    for elemento in lista:
        print(elemento)


# ******************** Plataforma y listas *****************#
plat1 = Plataforma("Playstation", False)
plat2 = Plataforma("Movil (Andoid / iOS)", True)
plat3 = Plataforma("Sega Saturn", False)
plat4 = Plataforma("Super Nintendo", False)
plat5 = Plataforma("PC", False)

list_plat1 = [plat1, plat2]  # La usa video1

list_plat2 = [plat3, plat4]  # La usan video2 y video3

list_plat3 = [plat5, plat1]  # La usa video4

list_plat4 = [plat2]  # La usa video5

list_plat5 = [plat1]  # La usa video7

list_plat6 = [plat1, plat5]  # La usa video6
# ******************************************************#

# ******************** Empresas y Distribuidoras ***************#
desa1 = Empresa("Rockstar North")
desa4 = Empresa("Rocksar Toronto")
distr1 = Empresa("Rockstar Games ✭ Capcom")

desa2 = Empresa("Midway Games")
distr2 = Empresa("Midway")

desa3 = Empresa("NetherRealm Studios")
distr3 = Empresa("Warner Bros. Interactive Enterteinment")
# **************************************************************#

# ****************************************** Videojuegos ********************************************************#
video1 = Videojuego("Grand Theft Auto - San Andreas", Genero.OTRO.name, list_plat1,
                    "Ambientada en Los Angeles de los 90s", 17.68, desa1, distr1, datetime.date(2004, 10, 26), 8.5)

video2 = Videojuego("Mortal Kombat II", Genero.LUCHA.name, list_plat2,
                    "La segunda edicion del torneo más importante entre los reinos", 90, desa2, distr2,
                    datetime.date(1993, 5, 3), 9)

video3 = Videojuego("Mortal Kombat 3", Genero.LUCHA.name, list_plat2, "Detén la invación de Shao Khan a la tierra", 90,
                    desa2, distr2, datetime.date(1995, 5, 15), 5.7)

video4 = Videojuego("Injustice 2", Genero.LUCHA.name, list_plat3,
                    "Elige entre dos bandos: los villanos o los superheores de DC", 57.80, desa3, distr3,
                    datetime.date(2017, 5, 6), 8)

video5 = Videojuego("Batman: Arkham Origins", Genero.ACCION_AVENTURAS.name, list_plat4,
                    "Adentrate en las profundidades de Gotham para conocer el origen del Joker", 2.66, desa3, distr3,
                    datetime.date(2013, 10, 16), 7.5)

video6 = Videojuego("Manhunt", Genero.OTRO.name, list_plat6,
                    "Un condenado a muerte es salvado de la inyeccion letal por un director de cine, pero a que costo...",
                    14.50, desa1, distr1, datetime.date(2003, 11, 18), 9)

video7 = Videojuego("The Warriors", Genero.ACCION_AVENTURAS.name, list_plat5,
                    "Basado en la pelicula homonima, ambientada 3 meses antes de la trama original", 36, desa4, distr1,
                    datetime.date(2005, 10, 17), 7.5)
# **************************************************************************************************************#

admin_video = videojuegosAdmin()
lista_vid = [video1, video2, video3, video4, video5, video6, video7]
for i in lista_vid:
    admin_video.agregar(i)

print("Lista de Juegos".center(50, "*"))
imprimir(admin_video)

print("Filtrar por desarrolladora".center(50, "*"))
lista1 = admin_video.filtrar_por_desarrolladora(desa3)
imprimir(lista1)

print("Filtrar por distribuidora".center(50, "*"))
lista2 = admin_video.filtrar_por_distribuidora(distr1)
imprimir(lista2)

print("Filtrar por genero".center(50, "*"))
lista3 = admin_video.filtrar_por_genero(Genero.LUCHA.name)
imprimir(lista3)

print("Cantidad de plataformas".center(50, "*"))
lista4 = admin_video.cantidad_por_plataforma()
print(lista4)
print("")

print("Ordenar por titulo".center(50, "*"))
admin_video.ordenar_titulo()
imprimir(admin_video)

print("Ordenar por Ranking".center(50, "*"))
admin_video.ordenar_mejores_primero()
imprimir(admin_video)
