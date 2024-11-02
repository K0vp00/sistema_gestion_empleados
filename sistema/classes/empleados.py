from classes.tipo_empleado import tipoEmpleado
from classes.estado import Estado
class Empleados(tipoEmpleado,Estado):
    def __init__(self, id, rut, nombre, direccion, telefono, correo, fecha_inicio, salario, fecha_nacimiento, contraseña, id_tipoEmpleado,id_estado):
        tipoEmpleado.__init__(self,id_tipoEmpleado)
        Estado.__init__(self,id_estado)
        self.__id = id
        self.__rut = rut
        self.__nombre = nombre
        self.__direccion = direccion
        self.__telefono = telefono
        self.__correo = correo
        self.__fecha_inicio = fecha_inicio
        self.__salario = salario
        self.__fecha_nacimiento = fecha_nacimiento
        self.__contraseña = contraseña


    @staticmethod #Para determinar el metodo como estatico y no depender de una instancia para su uso, falicitando el la pnatalla de inicio
    def validarDatos(rut, contrasena):
        from consultas_db import DB_consulta_validar
        from classes.empleados import Empleados
        query = "SELECT contrasena FROM EMPLEADOS WHERE rut = %s "
        resultado = DB_consulta_validar(query,rut)
        if resultado :
            hash_contrasena = resultado[0][0]
            return Empleados.validar_contrasena(contrasena,hash_contrasena)
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

class CRUD_empleados(Empleados): 

    @staticmethod
    def estado_empleado():#"eliminar" 
        from consultas_db import DB_actualizar
        rut_empleado = input('\nIngrese el RUT del empleado (con guion y digito verificador): ')
        dato = input('\nIngrese el valor\n1.- activado\n2.-deshabilitado\nOpcion: ')
        
        # Validar entrada de valor
        if dato not in ['1', '2']:
            print("Error: Debe ingresar 1 para habilitar o 2 para deshabilitar.")
            return
        query = "UPDATE empleados SET estado = %s WHERE rut = %s;"
        try:
            # Ejecuta la consulta con los valores como una tupla
            DB_actualizar(query,rut_empleado,dato)
            print('Estado actualizado exitosamente.')
        except Exception as e:
            print(f"Ocurrió un error al actualizar el estado: {e}")

    @staticmethod
    def crear_empleado():
        from consultas_db import DB_insertar
        from classes.empleados import Empleados
        from datetime import datetime
        try:
            rut = input("Ingrese el RUT del empleado: ")
            nombre = input("Ingrese el nombre del empleado: ")
            direccion = input("Ingrese la dirección del empleado: ")
            telefono = input("Ingrese el teléfono del empleado: ")
            correo = input("Ingrese el correo del empleado: ")

            fecha_inicio = input("Ingrese la fecha de inicio (año-mes-dia): ")
            fecha_inicio = datetime.strptime(fecha_inicio, '%Y-%m-%d')

            salario = int(input("Ingrese el salario del empleado: "))

            fecha_nacimiento = input("Ingrese la fecha de nacimiento (año-mes-dia): ")
            fecha_nacimiento = datetime.strptime(fecha_nacimiento, '%Y-%m-%d')

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
            encriptar_contrasena = Empleados.Encriptar(contrasena)
            values = (rut, nombre.lower(), direccion.lower(), telefono, correo.lower(), fecha_inicio, salario, fecha_nacimiento, encriptar_contrasena, id_tipoEmpleado, estado)

            DB_insertar(query,values)
            print("Empleado creado con éxito.")
        except ValueError as e:
            print(f"Error al ingresar datos numéricos: {e}. Por favor, intente nuevamente.")
               # Regresar al inicio del bucle para que el usuario intente de nuevo
        except Exception as e:
            print(f"Ocurrió un error: {e}. Por favor, intente nuevamente.")
           

    @staticmethod
    def ver_empleados():
        from consultas_db import DB_consulta
        query = '''SELECT rut, nombre,direccion, telefono, correo, DATE_FORMAT(fecha_inicio, '%d/%m/%Y'), salario, DATE_FORMAT(fecha_nacimiento, '%d/%m/%Y'), contrasena, id_tipoEmpleado, estado FROM EMPLEADOS'''
        DB_consulta(query)
