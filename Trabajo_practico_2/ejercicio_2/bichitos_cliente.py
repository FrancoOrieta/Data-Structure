from especie import Especie
from raza import Raza
from persona import Persona
from mascota import Mascota

def imprimir(lista: list):
    for mascota in lista:
        print(mascota)
        print("* Edad:", mascota.edad)
        print("")

def filtrar_gerontes(lista: list) -> list:
    boomer_pets = []
    for mascota in lista:
        if mascota.edad >= 13:
            boomer_pets.append(mascota)
    return boomer_pets

def filtro_especie(lista: list, especie: Especie):
    same_especie = []
    for mascota in lista:
        if mascota.raza.especie == especie:
            same_especie.append(mascota)
    return same_especie

def max_mascotero(lista: list) -> Persona:
    lista_duenios = []
    for mascota in lista:
        lista_duenios.append(mascota.dueño.dni)
    dni = max(set(lista_duenios), key = lista_duenios.count)
    for mascota in lista:
        if dni == mascota.dueño.dni:
            return mascota.dueño

especie1 = Especie("Canino")
especie2 = Especie("Felino")
especie3 = Especie("Reptil")

raza1 = Raza("Border Collie", especie1)
raza2 = Raza("Gato americano", especie2)
raza3 = Raza("Caniche", especie1)
raza4 = Raza("Tortuga", especie3)

dueño1 = Persona("Chuckie", "Devlin", 16809233)
dueño2 = Persona("Arbuckle", "Jon", 20806244)
dueño3 = Persona("Orieta", "Franco", 43609211)
dueño4 = Persona("Yoshi", "Hamato", 15205788)

mascota1 = Mascota(155, "Bingo", raza1, 1991, dueño1)
mascota2 = Mascota(12, "Garfield", raza2, 2018, dueño2)
mascota3 = Mascota(16, "Odie", raza1, 2018, dueño2)
mascota4 = Mascota(20, "Benji", raza3, 2014, dueño3)
mascota5 = Mascota(1, "Leonardo", raza4, 2008, dueño4)
mascota6 = Mascota(2, "Donatello", raza4, 2008, dueño4)
mascota7 = Mascota(3, "Raphael", raza4, 2007, dueño4)
mascota8 = Mascota(4, "Michelangelo", raza4, 2009, dueño4)

mascotas = [mascota1, mascota2, mascota3, mascota4, mascota5, mascota6, mascota7, mascota8]

print("")
print("Mascotas de la lista".center(50,"*"))
imprimir(mascotas)

print("")
print("Mascotas mayores de 13 años".center(50,"*"))
boomer_pets = filtrar_gerontes(mascotas)
imprimir(boomer_pets)

por_especies = filtro_especie(mascotas, especie1)
print("Solo Caninos".center(50,"*"))
imprimir(por_especies)

print("Dueño con más mascotas".center(50,"*"))
print(max_mascotero(mascotas))