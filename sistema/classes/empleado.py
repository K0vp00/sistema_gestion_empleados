
class Empleado():
    def __init__(self,rut, nombre, edad, salario, contrasena, tipo_empleado):
        self.rut = rut
        self.nombre = nombre
        self.edad = edad
        self.salario = salario
        self.contrasena = contrasena
        self.tipo_empleado = tipo_empleado
    
    @staticmethod
    def validarDatos(rut, contrasena):
        import mysql.connector
        import bcrypt
        try:
            # Conectar a la base de datos MySQL
            conexion = mysql.connector.connect(
                host="127.0.0.1", 
                user="root",
                password="",
                database="sistema_gestion_empleados" 
            )
            
            cursor = conexion.cursor()
            
            # Consulta para validar el rut y la contraseña
            consulta = "SELECT * FROM empleados WHERE rut = %s"
            
            contrasena = contrasena.encode()
            sal = bcrypt.gensalt()
            hashContrasena = bcrypt.hashpw(contrasena,sal)
            cursor.execute(consulta, (rut, hashContrasena))
            
            # Verificar si el usuario existe
            resultado = cursor.fetchone()
            
            if resultado:
                print("Inicio de sesión exitoso")
                return True
            else:
                print("Rut o contraseña incorrectos")
                return False

        except mysql.connector.Error as err:
            print(f"Error al conectar a la base de datos: {err}")
            return False
        
        finally:
            # Cerrar la conexión a la base de datos
            if conexion.is_connected():
                cursor.close()
                conexion.close()
