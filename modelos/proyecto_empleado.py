from proyectos import Proyectos
from empleados import Empleados
class proyectoEmpleado (Proyectos,Empleados):
    def __init__(self, id_proyectoEmpleado, id_proyecto, id_empleado):
        Proyectos.__init__(self,id_proyecto)
        Empleados.__init__(self,id_empleado)
        self.__idProyectoEmpleado = id_proyectoEmpleado