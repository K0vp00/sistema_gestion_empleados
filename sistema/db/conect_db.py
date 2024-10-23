import mysql.connector

config = {
    "host": "localhost",
    "user": "root",
    "password": "",
    "database": "gestion_empleados",
}

cnx = mysql.connector.connect(config)

if cnx and cnx.is_connected():

    with cnx.cursor() as cursor:

        result = cursor.execute("SELECT * FROM empleados")

        rows = cursor.fetchall()

        for rows in rows:

            print(rows)

    cnx.close()

else:

    print("Could not connect")