from empleado import Empleado
from consultas_db import DB_consulta
print('Bienvenido al sistema de EcoTech Solutions\nIngrese sus crecenciales')
Rut = input('Rut: ')
Clave = input('Clave: ')

if Empleado.validarDatos(Rut,Clave):
    print('Bienvenido a la plataforma')
    query = "SELECT c.tipo FROM empleado e INNER JOIN TipoEmpleado t on t.id_TipoEpleado = e.id_TipoEpleado "
    resultado = DB_consulta(query)
    if resultado == "":
        print
    elif resultado == "":
        print
    elif resultado == "":
        print
else:     
    print('Credenciales invalidas')
