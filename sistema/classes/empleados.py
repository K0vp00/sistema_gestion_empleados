class Empleado:

    @staticmethod #Para determinar el metodo como estatico y no depender de una instancia para su uso, falicitando el la pnatalla de inicio
    def validarDatos(rut, contrasena):
        from consultas_db import DB_consulta_validar
        from classes.empleados import Empleado
        query = "SELECT contrasena FROM EMPLEADOS WHERE rut = %s "
        resultado = DB_consulta_validar(query,rut)
        if resultado :
            hash_contrasena = resultado[0][0]
            return Empleado.validar_contrasena(contrasena,hash_contrasena)
        else:
            print('no se encontro el rut ingresado, intente de nuevo')
            return False
        
    @staticmethod
    def Encriptar(contrasena):
        import bcrypt
        hashContrasena = bcrypt.hashpw(contrasena.encode('utf-8'),bcrypt.gensalt())
        return hashContrasena.decode('utf-8')
    
    @staticmethod #"desencriptar" o valiadar si la contraseña es la misma
    def validar_contrasena(contrasena,hash_contrasena):
        import bcrypt
        if bcrypt.checkpw(contrasena.encode('utf-8'),hash_contrasena.encode()):
            print('Inicio exitoso')
            return True
        else:
            print('contraseña incorrecta')
            return False

class CRUD_empleados(Empleado): 

    @staticmethod
    def estado_empleado():#"eliminar" 
        from consultas_db import DB_actualizar
        rut_empleado = input('Ingrese el RUT del empleado (con guion y digito verificador): ')
        valor = input('Ingrese el valor(activado: 1/deshabilitado: 2): ')
        
        # Validar entrada de valor
        if valor not in ['1', '2']:
            print("Error: Debe ingresar 1 para habilitar o 2 para deshabilitar.")
            return

        query = "UPDATE empleados SET estado = %s WHERE rut = %s"
        try:
            # Ejecuta la consulta con los valores como una tupla
            DB_actualizar(query, (valor, rut_empleado))
            print('Estado actualizado exitosamente.')
        except Exception as e:
            print(f"Ocurrió un error al actualizar el estado: {e}")

    @staticmethod
    def crear_empleado():
        from consultas_db import DB_insertar
        from empleados import Empleado
        import datetime
        while True:
            try:
                rut = input("Ingrese el RUT del empleado: ")
                nombre = input("Ingrese el nombre del empleado: ")
                direccion = input("Ingrese la dirección del empleado: ")
                telefono = input("Ingrese el teléfono del empleado: ")
                correo = input("Ingrese el correo del empleado: ")

                fecha_inicio = input("Ingrese la fecha de inicio (año-mes-dia): ")
                fecha_inicio = datetime.strptime(fecha_inicio, '%Y-%m-%d').date()

                salario = int(input("Ingrese el salario del empleado: "))

                fecha_nacimiento = input("Ingrese la fecha de nacimiento (año-mes-dia): ")
                fecha_nacimiento = datetime.strptime(fecha_nacimiento, '%Y-%m-%d').date()

                contrasena = input("Ingrese la contraseña del empleado: ")
                id_tipoEmpleado = int(input("Ingrese el ID del tipo de empleado:\n 1.- Administrador\n2.- Desarrollador\n3.- Analista\n ID: "))        
                if id_tipoEmpleado not in [1, 2, 3]:
                    print("Error: Debe ingresar 1 para Administrador, 2 para Desarrollador o 3 para Analista.")
                    return
                estado = int(input("Ingrese el estado del empleado: 1.- activado\n2.- deshabilitado\nestado: "))
                if estado not in [1, 2]:
                    print("Error: Debe ingresar 1 para habilitar o 2 para deshababilitar.")
                    return
                query = '''INSERT INTO empleados (rut, nombre, direccion, telefono, correo, fecha_inicio, salario, fecha_nacimiento, contrasena, id_tipoEmpleado, estado)
                values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s );'''
                encriptar_contrasena = Empleado.Encriptar(contrasena)
                values = (rut, nombre.lower(), direccion.lower(), telefono, correo.lower(), fecha_inicio, salario, fecha_nacimiento, encriptar_contrasena, id_tipoEmpleado, estado)

                DB_insertar(query,values)
                print("Empleado creado con éxito.")
                break
            except ValueError as e:
                print(f"Error al ingresar datos numéricos: {e}. Por favor, intente nuevamente.")
                continue  # Regresar al inicio del bucle para que el usuario intente de nuevo
            except Exception as e:
                print(f"Ocurrió un error: {e}. Por favor, intente nuevamente.")
                continue

    @staticmethod
    def ver_empleados():
        from consultas_db import DB_consulta
        query = '''SELECT rut, nombre,direccion, telefono, correo, DATE_FORMAT(fecha_inicio, '%d/%m/%Y'), salario, DATE_FORMAT(fecha_nacimiento, '%d/%m/%Y'), contrasena, id_tipoEmpleado, estado FROM EMPLEADOS'''
        DB_consulta(query)
