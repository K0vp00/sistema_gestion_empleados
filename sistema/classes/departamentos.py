from empleados import Empleados
class Departamentos(Empleados):
    def __init__(self, id, nombre, telefono, id_empleado):
        super().__init__(id, nombre, telefono, id_empleado)
        self.__id = id
        self.__nombre = nombre
        self.__telefono = telefono
