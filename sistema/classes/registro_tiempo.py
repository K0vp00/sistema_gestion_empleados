from proyecto_empleado import proyectoEmpleado
class registroTiempo(proyectoEmpleado):
    def __init__(self, id_nombre, nombre, direccion, telefono, correo, fecha_inicio, salario,id_proyectoEmpleado):
        super().__init__(self,id_proyectoEmpleado)
        self.__id_nombre = id_nombre
        self.__nombre = nombre
        self.__direccion = direccion
        self.__telefono = telefono
        self.__correo = correo
        self.__fecha_inicio = fecha_inicio
        self.__salario = salario
        
