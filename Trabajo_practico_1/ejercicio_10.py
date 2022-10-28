from funciones import interface_MENU_Entrada, añadir_empleado_MENU, borrar_empleado_MENU, ordenar_Legajo_MENU, ordenar_Apellido_Y_Nombre_MENU, imprimir_Lista_MENU, interface_MENU_Salida
Empleados = []

opcion = interface_MENU_Entrada()
while opcion != 0:
    match opcion:
        case 1:
            Empleados = añadir_empleado_MENU()
        case 2:
            Empleados = borrar_empleado_MENU(Empleados)
        case 3:
            Empleados = ordenar_Legajo_MENU(Empleados)
        case 4:
            Empleados = ordenar_Apellido_Y_Nombre_MENU(Empleados)
        case 5:
            imprimir_Lista_MENU(Empleados)

    opcion = interface_MENU_Salida()