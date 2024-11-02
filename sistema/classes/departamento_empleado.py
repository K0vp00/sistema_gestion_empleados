from empleados import Empleados
from departamentos import Departamentos
class departamentoEmpleado(Empleados,Departamentos):
    def __init__(self, id_departamentoEmpleado, id_departamento, id_empleado):
        Empleados.__init__(self, id, id_empleado)
        Departamentos.__init__(self, id, id_departamento)
        self.__id_departamentoEmpleado = id_departamentoEmpleado