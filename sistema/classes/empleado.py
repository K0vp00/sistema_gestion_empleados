
class Empleado():
    def __init__(self,rut, nombre, edad, salario, contrasena, tipo_empleado):
        self.rut = rut
        self.nombre = nombre
        self.edad = edad
        self.salario = salario
        self.contrasena = contrasena
        self.tipo_empleado = tipo_empleado
    
    @staticmethod #Para detarminar el metodo como estatico y no depender de una instancia para su uso, falicitando el la pnatalla de inicio
    def validarDatos(rut, contrasena):
        from consultas_db import DB_consulta
        import bcrypt
        if resultado :
            query = f"SELECT RUT FROM EMPLEADOS WHERE rut = {rut} "
            resultado = DB_consulta(query)
            contrasena = contrasena.encode()
            sal = bcrypt.gensalt()
            hashContrasena = bcrypt.hashpw(contrasena,sal)
            if bcrypt.checkpw(hashContrasena.encode(),resultado.encode()):
                return True
            else:
                print('contraseña incorrecta')
                return False
        else:
            print('no se encontro el rut ingresado, intente de nuevo')
            return False