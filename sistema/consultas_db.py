# esta unica funcion se encarga de conectar y consultar datos con la bd, con esto implementamos mas seguridad y reducimos la posibilidad de errores
def DB_consulta(Consulta): 
    from conect_db import config
    import mysql.connector   
    cnx = mysql.connector.connect(**config)

    cursor = cnx.cursor()

    if cnx and cnx.is_connected():

        with cnx.cursor() as cursor:

            result = cursor.execute(Consulta)

            rows = cursor.fetchall()

            for rows in rows:

                print(rows)

        cnx.close()

    else:

        print("No se pudo conectar")

    cursor.close()
    cnx.close()

#prueba de conexion con base de datos
query = ("SELECT rut, nombre, direccion, telefono, correo FROM empleado WHERE rut = '12.234.567-7';")
DB_consulta(query)