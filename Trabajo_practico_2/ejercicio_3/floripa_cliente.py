import datetime
from marcacion import Marcacion
from oficina import Oficina
from empleado import Empleado
from marcacionTipo import MarcacionTipo
from marcacionAdmin import MarcacionAdmin

def imprimir(lista):
    for elemento in lista:
        print(elemento)
        print("")

ofi1 = Oficina("contabilidad", datetime.time(13,00),datetime.time(21,00))
ofi2 = Oficina("RR.HH", datetime.time(10,00),datetime.time(22,00))

emp1 = Empleado(864, 26893041, "Lombardo","Mauro Ezequiel", ofi1)
emp2 = Empleado(222, 22074884, "Acosta","Alejo Nahuel", ofi1)
emp3 = Empleado(701, 29440433, "Palacios","Mateo", ofi2)
emp4 = Empleado(563, 21562597, "Herrera","Mauro Román", ofi2)
emp5 = Empleado(119, 24007151, "Conde","Gonzalo", ofi1)

mar1 = Marcacion(emp1, datetime.datetime(2022,9,13, 12,50), MarcacionTipo.ENTRADA.name)
mar2 = Marcacion(emp1, datetime.datetime(2022,9,13, 19,30), MarcacionTipo.SALIDA.name)

mar3 = Marcacion(emp2, datetime.datetime(2022,9,13, 15,30), MarcacionTipo.ENTRADA.name) #mar3 Tarde
mar4 = Marcacion(emp2, datetime.datetime(2022,9,13, 23,30), MarcacionTipo.SALIDA.name)

mar5 = Marcacion(emp3, datetime.datetime(2022,9,13, 9,50), MarcacionTipo.ENTRADA.name)
mar6 = Marcacion(emp3, datetime.datetime(2022,9,13, 21,50), MarcacionTipo.SALIDA.name)

mar7 = Marcacion(emp4, datetime.datetime(2022,9,13, 10,30), MarcacionTipo.ENTRADA.name) #mar7 Tarde
mar8 = Marcacion(emp4, datetime.datetime(2022,9,13, 22,15), MarcacionTipo.SALIDA.name)

mar9 = Marcacion(emp5, datetime.datetime(2022,9,13, 13,15), MarcacionTipo.ENTRADA.name) #mar9 Tarde
mar10 = Marcacion(emp5, datetime.datetime(2022,9,13, 21,15), MarcacionTipo.SALIDA.name)

mar11 = Marcacion(emp1, datetime.datetime(2022,9,14, 14,00), MarcacionTipo.ENTRADA.name) #mar11 Tarde
mar12 = Marcacion(emp1, datetime.datetime(2022,9,14, 21,15), MarcacionTipo.SALIDA.name)

mar13 = Marcacion(emp2, datetime.datetime(2022,9,14, 12,30), MarcacionTipo.ENTRADA.name)
mar14 = Marcacion(emp2, datetime.datetime(2022,9,14, 20,30), MarcacionTipo.SALIDA.name)

mar15 = Marcacion(emp3, datetime.datetime(2022,9,14, 9,50), MarcacionTipo.ENTRADA.name)
mar16 = Marcacion(emp3, datetime.datetime(2022,9,14, 21,30), MarcacionTipo.SALIDA.name)

marcacion_admin = MarcacionAdmin()

lista_Auxiliar = [mar1, mar2, mar3, mar4, mar5, mar6, mar7, mar8, mar9, mar10, mar11, mar12, mar13, mar14, mar15, mar16]
for i in lista_Auxiliar:
    marcacion_admin.agregar(i)

print("Lista de marcaciones".center(50,"*"))
imprimir(marcacion_admin)

print("Empleados totales".center(50,"*"))
lista2 = marcacion_admin.empleados()
imprimir(lista2)

print("Filtrar por empleado".center(50,"*"))
lista3 = marcacion_admin.filtrar_por_empleado(emp2)
imprimir(lista3)

print("Filtrar por Tipo".center(50,"*"))
lista4 = marcacion_admin.filtrar_por_tipo(MarcacionTipo.ENTRADA.name)
imprimir(lista4)

print("Empleados que llegaron tarde".center(50,"*"))
lista5 =  marcacion_admin.llegadas_tarde()
imprimir(lista5)

print("Ordenar por legajo".center(50,"*"))
marcacion_admin.ordenar_legajo()
imprimir(marcacion_admin)

print("Ordenar por nombre".center(50,"*"))
marcacion_admin.ordenar_apellido_nombre()
imprimir(marcacion_admin)