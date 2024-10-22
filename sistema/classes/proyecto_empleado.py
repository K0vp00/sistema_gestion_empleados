from proyecto import proyecto
class proyectoEmpleado (proyecto):
    def __init__(self, id_proyectoEmpleado, id_proyecto, id_empleado):
        proyecto.__init__(self,)
        self.__idProyectoEmpleado = id_proyectoEmpleado
        self.__id_proyecto = id_proyecto
        self.__id_empleado = id_empleado