def encriptacion_contrasenas_DB():
    # Encriptar contraseñas de la base de datos
    from classes.empleados import Empleados
    from consultas_db import DB_actualizar

    contrasenas = [
        "Mperez85!",
        "Jsoto456#",
        "LHerrera789&",
    ]
    
    empleados = [
        "12345678-4",
        "20765432-7",
        "18654321-6",
    ]

    query = "UPDATE empleados SET contrasena = %s WHERE rut = %s"

    for i in range(len(contrasenas)):
        # Encriptar la contraseña
        contrasena_encriptada = Empleados.Encriptar(contrasenas[i])
        # Actualizar la base de datos con el RUT y la contraseña encriptada
        DB_actualizar(query,empleados[i], contrasena_encriptada )