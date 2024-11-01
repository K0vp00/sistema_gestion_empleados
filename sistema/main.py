
def iniciar_sesion():
    from empleados import Empleado
    import getpass
    print('Bienvenido al sistema de EcoTech Solutions\nIngrese sus credenciales')
    rut = input('Rut (con guion y digito verificador): ')
    contrasena = getpass.getpass("Introduce tu contraseña: ")
    if Empleado.validarDatos(rut,contrasena):
         print('Bienvenido, usuario autenticado')
         return rut
    else:     
        print('Credenciales invalidas')
        return


def interfaz(rut):
    from consultas_db import DB_consulta_validar
    from empleados import CRUD_empleados
    from classes.informe import Informe
    from classes.proyectos import Proyectos
    print('Plataforma EcoTech Solutions')
    query = "SELECT t.tipo FROM empleados e INNER JOIN tipoEmpleado t ON t.id_tipoEmpleado = e.id_tipoEmpleado where rut = ?;"
    resultado = DB_consulta_validar(query,rut)
    if resultado:
        tipo_empleado = resultado[0]

        if tipo_empleado == "Administrador":
            opcion = input('Elija una de las siguientes opciones: \n1.- Gestion empleados\n2.- Gestion informes\n3.- Gestion proyectos\nOpción: ')
            if opcion == '1':
                opcion = input('Elija una de las siguientes opciones: \n1.- Ingresar empleado\n2.- Cambiar estado (eliminar)\n3.- Ver empleados\nOpción: ')
                if opcion == "1":
                    CRUD_empleados().crear_empleado()
                elif opcion == "2":
                    CRUD_empleados().estado_empleado()
                elif opcion == "3":
                    CRUD_empleados().ver_empleados()
                else:
                    print("Opción inválida.")

            elif opcion == "2":
                opcion = input('Elija una de las siguientes opciones: \n1.- crear informe\n2.- Ver informe\nOpción: ')
                if opcion == "1":
                    Informe().crear_informe()
                elif opcion == "2":
                    Informe().ver_informes()
                else:
                    print("Opción inválida.")
                
            elif opcion == "3":
                opcion = input('Elija una de las siguientes opciones: \n1.- crear proyecto\n2.- Ver proyectos\nOpción: ')
                if opcion == "1":
                    Proyectos().crear_proyecto()
                elif opcion == "2":
                    Proyectos().ver_proyectos()
                else:
                    print("Opción inválida.")
            else:
                print("Opción inválida.")


        elif tipo_empleado == "desarrollador":
            opcion = input('Elija una de las siguientes opciones: \n1.- crear proyecto\n2.- Ver proyectos\nOpción: ')
            if opcion == "1":
                Proyectos().crear_proyecto()
            elif opcion == "2":
                Proyectos().ver_proyectos()
            else:
                print("Opción inválida.")

        elif tipo_empleado == "Analista":
            opcion = input('Elija una de las siguientes opciones: \n1.- crear informe\n2.- Ver informe\nOpción: ')
            if opcion == "1":
                Informe().crear_informe()
            elif opcion == "2":
                Informe().ver_informes()
            else:
                print("Opción inválida.")
        else:
            return
    else:
        print("No se encontró el tipo de empleado asociado al RUT ingresado.")