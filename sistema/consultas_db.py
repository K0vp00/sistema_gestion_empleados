

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

#pruba de conexion con base de datos
query = ("SELECT * FROM empleado WHERE rut = '12345678-9';")
DB_consulta(query)