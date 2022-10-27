import random
from operator import itemgetter
# -------------------------------------------------------------- # Funciones usadas en el ejercicio 5
def generar_random(a, b):
    if a < b:
        numero = random.randint(a,b)
    else:
        numero = random.randint(b,a)
    return numero

def advinar_numero(a, num_maquina):
    if a == num_maquina:
        print("Correcto!! has ganado")
        return True
    elif a < num_maquina:
        print("El numero ingresado es menor")
        return False
    else:
        print("El numero ingresado es mayor")
        return False

def jugar(num_j, num_m):
    aux = False
    while aux != True:
        aux = advinar_numero(num_j, num_m)
        if aux == False:
            num_j = int(input("Intentalo de nuevo\n"))
        else:
            continue
# -------------------------------------------------------------- #

# -------------------------------------------------------------- # Funcion usada en el ejercicio 7
def buscar_en_lista(a, lista):
    for i in range(0, len(lista)):
        if a == lista[i]:
            return i
        else:
            continue
    return -1
# -------------------------------------------------------------- #

# -------------------------------------------------------------- # Funciones usadas en el ejercicio 8
def ingresar_Ciudades(res, lista):
    if res == "si" or res == "Si" or res == "SI" or res == "y" or res == "Y" or res == "yes" or res == "Yes" or res == "YES" or res == "s" or res == "S":
        cortar = False
        print("Continue enumerando ciudades o escriba no para salir")
        while cortar == False:
            res = input("")
            if res != "no" and res != "No" and res != "NO" and res != "n" and res != "N":
                lista.append(res)
            else:
                cortar = True
                return lista

    else:
        return lista

def imprimir_Ciudades(lista):
    print("")
    print("Total de ciudades ingresadas: " + str(len(lista)))
    print("Listado: ")
    for i in range(0, len(lista)):
        print(lista[i])
# -------------------------------------------------------------- #

# -------------------------------------------------------------- # Funciones usadas en el ejercicio 10
STORAGE_FILE = []  #Variable STORAGE_FILE

def generar_legajo():
    legajo = random.randint(1000,9999)
    if legajo not in STORAGE_FILE:      #Cuando se genera un legajo aleatorio
        STORAGE_FILE.append(legajo)     #se pregunta si este no está almacenado en STORAGE_FILE (referenciando a la variable global)
        return legajo                   #si el legajo ya existe se genera otro, hasta que sea distinto a cualquier legajo en STORAGE_LEGAJO
    else:
        generar_legajo()

def añadir_empleado(nombre, apellido, camisa, pantalon, zapatos):
    legajo = generar_legajo()
    dict = {"Legajo":legajo, "Nombre":nombre, "Apellido":apellido, "Camisa":camisa, "Pantalón":pantalon, "Zapatos de seguridad":zapatos}
    return dict

def borrar_empleado(i, lista):
    if i < len(lista):
        del lista[i]
        return lista
    else:
        exit

def interface_MENU_Entrada():
    print("")
    print("Bienvenido al menu de inicio")
    print("Elige la operacion que deseas realizar")
    print("---------------------")
    print("1: Ingresar empleados\n" +
        "2: Borrar empleados\n" +
        "3: Ordenar por legajo\n" +
        "4: Ordenar por nombre y apellido\n" +
        "5: Imprimir lista de empleados\n" +
        "0: Salir")
    print("---------------------")
    menu = int(input(""))
    print("")
    return menu

def añadir_empleado_MENU():
    lista_Principal = []
    cortar = False

    while cortar == False: 
        nombre = input("Ingresar nombre: ")
        apellido = input("Ingresar apellido: ")
        cam_talle = int(input("Ingresar talle de camisa: "))
        pant_talle = int(input("Ingresar talle de panatalón: "))
        zapatos = bool(int(input("¿Usa zapatos de seguridad? (1: si, 0: no): ")))
        
        empleado = añadir_empleado(nombre, apellido, cam_talle, pant_talle, zapatos)
        lista_Principal.append(empleado)

        print("")
        ans = input("¿Desea ingresar un nuevo empleado? y/n\n")
        if ans == "y" or ans == "Y":
            print("")
            continue
        else:
            cortar = True
            return lista_Principal

def borrar_empleado_MENU(lista_Principal):
    cortar = False

    while cortar == False:
        indice = int(input("¿Que empleado desea borrar? ingrese un numero\n"))
        lista_Principal = borrar_empleado(indice, lista_Principal)

        ans = input("¿Desea quitar otro empleado de la lista? y/n\n")
        if ans == "y" or ans == "Y":
            print("")
            continue
        else:
            cortar = True
            return lista_Principal

def ordenar_Legajo_MENU(lista_Principal):
    lista_Ordenada = sorted(lista_Principal, key = itemgetter("Legajo"))
    return lista_Ordenada

def ordenar_Apellido_Y_Nombre_MENU(lista_Princial):
    lista_Ordenada = sorted(lista_Princial, key = itemgetter("Apellido", "Nombre"))
    return lista_Ordenada

def imprimir_Lista_MENU(lista_Principal):
    for i in range(0, len(lista_Principal)):
        print(lista_Principal[i])

def interface_MENU_Salida():
    print("")
    print("¿Desea realizar otra operación?")
    print("---------------------")
    print("1: Ingresar empleados\n" +
        "2: Borrar empleados\n" +
        "3: Ordenar por legajo\n" +
        "4: Ordenar por nombre y apellido\n" +
        "5: Imprimir lista de empleados\n" +
        "0: Salir")
    print("---------------------")
    menu = int(input(""))
    return menu
# -------------------------------------------------------------- #