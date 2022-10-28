from categoria import Categoria
from autor import Autor
from libro import Libro

cat1 = Categoria("Cuento", "Literatura del absurdo")
autor1 = Autor("Kafka", "Franz")
libro1 = Libro(167, "La Metamorfosis", autor1, cat1, 1916)

cat2 = Categoria("Cuento", "Literatura policial")
autor2 = Autor("Borges", "Jorge Luis")
libro2 = Libro(199, "El jardin de senderos que se bifurcan", autor2, cat2, 1941)

cat3 = Categoria("Terror", "Ciencia Ficción")
autor3 = Autor("Lovecraft", "Howard Phillips")
libro3 = Libro(178, "La llamada de Cthulhu", autor3, cat3, 1928)

cat4 = Categoria("Cuento")
libro4 = Libro(170, "El fin", autor2, cat4, 1953)

cat5 = Categoria("Terror", "Novela", "Gotica")
autor5 = Autor("Wilde", "Oscar")
libro5 = Libro(179, "El retrato de Dorian Gray", autor5, cat5, 1890)

def imprimir(libros : list):
    for libro in libros:
        print(libro)
        print(" ")

def filtrar_por_anio(libros, anio):
    lib_nuevo = []
    for libro in libros:
        if anio == libro.anio_de_publicación:
            lib_nuevo.append(libro)
    return lib_nuevo

def filtrar_por_categoria(libros, cat : Categoria):
    lib_nuevo = []
    for libro in libros:
        if cat.nombre == libro.categoria.nombre:
            lib_nuevo.append(libro)
    return lib_nuevo

def filtrar_por_autor(libros, autor : Autor):
    lib_nuevo = []
    for libro in libros:
        if autor.apellido == libro.Autor.apellido and autor.nombre == libro.Autor.nombre:
            lib_nuevo.append(libro)
    return lib_nuevo


lib = [libro1, libro2, libro3, libro4, libro5]

print("Lista de Libros".center(50, "*"))
imprimir(lib)

print("Filtrar por año".center(50, "*"))
nueva = filtrar_por_anio(lib, 1916)
imprimir(nueva)

print("Filtrar por categoria".center(50, "*"))
nueva = filtrar_por_categoria(lib, cat4)
imprimir(nueva)

print("Filtrar por autor".center(50, "*"))
nueva = filtrar_por_autor(lib, autor2)
imprimir(nueva)