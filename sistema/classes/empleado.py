class Empleado():
    
    @staticmethod #Para determinar el metodo como estatico y no depender de una instancia para su uso, falicitando el la pnatalla de inicio
    def validarDatos(rut, contrasena):
        from consultas_db import DB_consulta
        import bcrypt
        if resultado :
            query = f"SELECT contrasena FROM EMPLEADOS WHERE rut = {rut} "
            resultado = DB_consulta(query)
            contrasena = contrasena.encode()
            sal = bcrypt.gensalt()
            hashContrasena = bcrypt.hashpw(contrasena,sal)
            #hashContrasena = bcrypt.hashpw(contrasena.encode('utf-8'),bcrypt.gensalt())
            #if bcryt.checkpw(contrasena.encode('utf-8'),hashContrasena)
            if bcrypt.checkpw(hashContrasena.encode(),):# la propia libreria compara las contraseñas sin necesidad de desencriptar y evitar posibles problemas de seguridad
                return True
            else:
                print('contraseña incorrecta')
                return False
        else:
            print('no se encontro el rut ingresado, intente de nuevo')
            return False
        
    class Encriptar:
        