import mysql.connector

'''# Connect to server
cnx = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database = "Gestion_empleados")

# Get a cursor
cur = cnx.cursor()

# Execute a query
cur.execute("SELECT * FROM EMPLADOS()")

# Fetch one result
row = cur.fetchone()
print("Current date is: {0}".format(row[0]))

# Close connection
cnx.close()'''


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