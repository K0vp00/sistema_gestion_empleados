from classes.empleados import Empleados
class Informe(Empleados):
    def __init__(self, id, nombre_informe, fecha_creacion, id_empleado):
        super().__init__(self,id_empleado)
        self.__id = id
        self.__nombre_informe = nombre_informe
        self.__fecha_creacion = fecha_creacion
        


    @staticmethod
    def ver_informes():
        from consultas_db import DB_consulta
        query = "SELECT nombre_informe, DATE_FORMAT(fecha_creacion, '%d/%m/%Y') as fecha_creacion, id_empleado FROM informe;"
        DB_consulta(query)
    
    @staticmethod
    def crear_informe():
        from consultas_db import DB_insertar
        import datetime
        while True:
            try:
                nombre_informe = input("Ingrese el nombre: ")
                fecha_creacion = input("Ingrese la fecha de creación (año/mm/dia): ")
                fecha_creacion = datetime.datetime.strptime(fecha_creacion, '%Y/%m/%d')
                id_empleado = input("Ingrese el ID del empleado: ")
                query = '''INSERT INTO empleados (nombre_informe, fecha_creacion, id_empleado)values (?, ?, ?);'''
                values = (nombre_informe.lower(), fecha_creacion, id_empleado)

                DB_insertar(query,values)

                print("informe creado con éxito.")
                break
            except ValueError as e:
                print(f"Error al ingresar datos: {e}. Por favor, intente nuevamente.")
                continue  # Regresar al inicio del bucle para que el usuario intente de nuevo
            except Exception as e:
                print(f"Ocurrió un error: {e}. Por favor, intente nuevamente.")
                continue