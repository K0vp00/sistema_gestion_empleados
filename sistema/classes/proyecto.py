import datetime
class Proyecto():
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
            return True
        except ValueError:
            return print('Formato de fecha incorrecto')
        
    def CRUD (self):

        def create(proyecto):
            
            print('Proyecto creado con exito')

        def Read():
            
            ifoProyectos = ('''SELECT ID_PROYECTO, 
                            NOMBRE,
                            DESCRIPCION,
                            FECHA_INICIO,
                            FECHA_FIN 
                            FROM PROYECTO''') 
            return 
        