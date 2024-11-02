from modulos import Modulos
from empleados import Empleados
class Accesos(Modulos,Empleados):
    def __init__(self, id_accesos, id_modulo, id_empleado):
        Modulos.__init__(self, id, id_modulo)
        Empleados.__init__(self, id, id_empleado)
        self.__id_accesos = id_accesos
