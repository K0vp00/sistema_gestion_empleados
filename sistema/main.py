from encriptar import encriptacion_contrasenas_DB
def interfaz(rut):
    from consultas_db import DB_consulta_validar
    from classes.empleados import CRUD_empleados
    from classes.informe import Informe
    from classes.proyectos import Proyectos
    print('\n--------------------------------------------\n|Plataforma EcoTech Solutions|\n--------------------------------------------\n')
    query = "SELECT t.tipo FROM empleados e INNER JOIN tipoEmpleado t ON t.id_tipoEmpleado = e.id_tipoEmpleado where rut = %s;"
    resultado = DB_consulta_validar(query,rut)
    if resultado:
        tipo_empleado = resultado[0][0]

        if tipo_empleado == "Administrador":
            opcion = input('Elija una de las siguientes opciones: \n1.- Gestion empleados\n2.- Gestion informes\n3.- Gestion proyectos\n4.- Salir\nOpción: ')
            if opcion == '1':
                opcion = input('Elija una de las siguientes opciones: \n1.- Ingresar empleado\n2.- Cambiar estado (eliminar)\n3.- Ver empleados\nOpción: ')
                if opcion == "1":
                    CRUD_empleados.crear_empleado()
                    interfaz(rut)
                elif opcion == "2":
                    CRUD_empleados.estado_empleado()
                    interfaz(rut)
                elif opcion == "3":
                    CRUD_empleados.ver_empleados()
                    interfaz(rut)
                else:
                    print("Opción inválida.")

            elif opcion == "2":
                opcion = input('Elija una de las siguientes opciones: \n1.- crear informe\n2.- Ver informe\nOpción: ')
                if opcion == "1":
                    Informe.crear_informe()
                    interfaz(rut)
                elif opcion == "2":
                    Informe.ver_informes()
                    interfaz(rut)
                else:
                    print("Opción inválida.")
                
            elif opcion == "3":
                opcion = input('Elija una de las siguientes opciones: \n1.- crear proyecto\n2.- Ver proyectos\nOpción: ')
                if opcion == "1":
                    Proyectos.crear_proyecto()
                    interfaz(rut)
                elif opcion == "2":
                    Proyectos.ver_proyectos()
                    interfaz(rut)
                else:
                    print("Opción inválida.")
            elif opcion == "4":
                print("Saliendo del sistema")
            else:
                print("Opción inválida.")


        elif tipo_empleado == "Desarrollador":
            opcion = input('Elija una de las siguientes opciones: \n1.- crear proyecto\n2.- Ver proyectos\nOpción: ')
            if opcion == "1":
                Proyectos.crear_proyecto()
                interfaz(rut)
            elif opcion == "2":
                Proyectos.ver_proyectos()
                interfaz(rut)
            else:
                print("Opción inválida.")

        elif tipo_empleado == "Analista":
            opcion = input('Elija una de las siguientes opciones: \n1.- crear informe\n2.- Ver informe\nOpción: ')
            if opcion == "1":
                Informe.crear_informe()
                interfaz(rut)
            elif opcion == "2":
                Informe.ver_informes()
                interfaz(rut)
            else:
                print("Opción inválida.")
        else:
            return
    else:
        print("No se encontró el tipo de empleado asociado al RUT ingresado.")

def iniciar_sesion():
    from classes.empleados import Empleados
    from consultas_db import DB_consulta_validar
    import getpass

    print('--------------------------------------------\n|Bienvenido al sistema de EcoTech Solutions|\n--------------------------------------------\n\nIngrese sus credenciales: \n')

    rut = input('Rut (con guion y digito verificador): ')
    query = "SELECT nombre_estado FROM empleados emp INNER JOIN estado est ON emp.estado = est.id_estado WHERE rut = %s;"
    resultado = DB_consulta_validar(query,rut)
    estado = resultado[0][0].strip().lower() if resultado else None
    if estado == 'activo':
        contrasena = getpass.getpass("Introduce tu contraseña: ")
        if Empleados.validarDatos(rut,contrasena):
            print('\nBienvenido')
            interfaz(rut)
            return
    elif estado == "deshabilitado": 
        print('Cuenta deshabilitada. ¡Actualice el estado, si se utilizara la cuenta!')
    else:
        print("¡Hasta luego!")


#Datos para pruebas
''' maria perez "activo" (adm)
    rut: 12345678-4
    clave: Mperez85!
    '''

'''juan soto "desabilitado" (analista)
    rut: 20765432-7 
    clave: Jsoto456#
    '''

''' luis herrera "activo" (desarrollador)
    rut: 18654321-6
    clave: Jsoto456#
    '''

'''iniciar una sola vez encriptacion_contrasenas_DB para actualizar la contraseña de texto a encriptada dsp de pegar los script (DDL,DML) en la BD. Para el uso del main (interfaz)'''
#encriptacion_contrasenas_DB()
iniciar_sesion()