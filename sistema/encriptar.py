def DB_consulta_validar(Consulta, rut): 
    from conect_db import config
    import mysql.connector   
    cnx = None
    cursor = None    
    try:
        # Establecer conexión
        cnx = mysql.connector.connect(**config)
        if cnx.is_connected():
            cursor = cnx.cursor()
            
            # Ejecutar la consulta pasando 'rut' como tupla
            cursor.execute(Consulta, (rut,))

            # Obtener los resultados
            rows = cursor.fetchall()
            if rows:
                return rows  # Retorna los resultados si se encuentran
            else:
                print("No se encontraron resultados para el RUT proporcionado.")
                return None

    except mysql.connector.Error as e:
        print("Error al conectar o ejecutar la consulta en MySQL:", e)
        return None

    finally:
        # Cerrar el cursor y la conexión si están abiertos
        if cursor:
            cursor.close()
        if cnx:
            cnx.close()
            print("Conexión cerrada")

rut = input('Rut (con guion y digito verificador): ')
query = "SELECT nombre_estado FROM empleados emp INNER JOIN estado est ON emp.estado = est.id_estado WHERE rut = %s;"
if DB_consulta_validar(query,rut) == 'activo':
    print('El empleado esta activo')
else:
    print('El empleado esta deshabilitado')