import datetime
class Proyectos():
    def __init__(self,id_proyecto, nombre, descripcion, fecha_inicio, fecha_fin):
        self.__id_proyecto = id_proyecto
        self.__nombre = nombre
        self.__descripcion = descripcion
        self.__fecha_inicio = fecha_inicio
        self.__fecha_fin = fecha_fin

    def validarFecha(self):
        try:
            fecha_inicio = datetime.datetime.strptime(self.__fecha_inicio, '%Y-%m-%d').date()
            fecha_fin = datetime.datetime.strptime(self.__fecha_fin, '%Y-%m-%d').date()
            if fecha_fin < fecha_inicio:
                return False
            return fecha_inicio,fecha_fin
        except ValueError:
            return print('Formato de fecha incorrecto')
        
    @staticmethod
    def ver_proyectos():
        from consultas_db import DB_consulta
        query = '''SELECT nombre, descripcion, DATE_FORMAT(fecha_inicio, '%d/%m/%y') as fecha_inicio, DATE_FORMAT(fecha_fin, '%d/%m/%y') as fecha_fin FROM proyectos;'''
        DB_consulta(query)
    
    @staticmethod
    def crear_proyecto():
        from consultas_db import DB_insertar
        import datetime
        while True:
            try:
                nombre = input("Ingrese el nombre: ")
                descripcion = input("Ingrese la descripción del proyecto: ")
                fecha_inicio = input("Ingrese la fecha de inicio del proyecto (YYYY-MM-DD): ")
                fecha_inicio = datetime.datetime.strptime(fecha_inicio, '%Y-%m-%d').date()
                fecha_fin = input("Ingrese la fecha de fin del proyecto (YYYY-MM-DD): ")
                fecha_fin = datetime.datetime.strptime(fecha_fin, '%Y-%m-%d').date()
                query = '''INSERT INTO proyectos (nombre, descripcion, fecha_inicio, fecha_fin)
                values (%s, %s, %s, %s);'''
                values = (nombre.lower(),descripcion.lower(), fecha_inicio, fecha_fin)

                DB_insertar(query,values)

                print("proyecto creado con éxito.")
                break
            except ValueError as e:
                print(f"Error al ingresar datos: {e}. Por favor, intente nuevamente.")
                continue  # Regresar al inicio del bucle para que el usuario intente de nuevo
            except Exception as e:
                print(f"Ocurrió un error: {e}. Por favor, intente nuevamente.")
                continue
        