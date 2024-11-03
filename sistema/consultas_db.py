# Funcion para la validacion de datos con la BD
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
# Funcion para Consultar datos en la BD
def DB_consulta(Consulta): 
    from conect_db import config
    import mysql.connector 
    cnx = None
    cursor = None    
    try:  
        cnx = mysql.connector.connect(**config)
        cursor = cnx.cursor()
        if cnx and cnx.is_connected():
            with cnx.cursor() as cursor:
                cursor.execute(Consulta)
                # Obtener y mostrar los nombres de las columnas
                columnas = [desc[0] for desc in cursor.description]
                print(" | ".join(columnas))  # Imprime los nombres de las columnas
                print("-" * 50)  # Línea separadora
        
                # Obtener los resultados
                rows = cursor.fetchall()
                for row in rows:
                    print(" | ".join(map(str, row)))# Convertir cada valor a cadena y unir
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        if 'cnx' in locals() and cnx.is_connected():
            cnx.close()
            
# Funcion para insertar datos a la BD
def DB_insertar(query,values):
    import mysql.connector
    from mysql.connector import Error
    from conect_db import config
    cnx = None
    cursor = None
    try:
        cnx = mysql.connector.connect(**config)
        if cnx.is_connected():
            cursor = cnx.cursor()
            cursor.execute(query,values)
            # Confirmar los datos para que queden guardados y no se suban de manera temporal a la bd
            cnx.commit()
            # Obtener el ID de la última fila insertada
            ultimo_id_insertado = cursor.lastrowid
            print("Datos insertados con éxito. ID de la última fila:", ultimo_id_insertado)
            return ultimo_id_insertado

    except Error as e:
        print("Error al conectar con MySQL", e)

    finally:
        if cursor:
            cursor.close()
        if cnx and cnx.is_connected():
            cnx.close()
            
# Funcion para actualizar datos en la BD
def DB_actualizar(query,dato,rut):
    import mysql.connector
    from mysql.connector import Error
    from conect_db import config
    cnx = None
    cursor = None
    try:
        cnx = mysql.connector.connect(**config)

        if cnx.is_connected():
            cursor = cnx.cursor()
        
            cursor.execute(query,(dato,rut))
            
            # Confirmar los cambios para que se guarden
            cnx.commit()
            
            # Obtener el recuento de las filas afectadas
            filas_afectadas = cursor.rowcount

            if filas_afectadas > 0:
                print(f"{filas_afectadas} fila(s) actualizada(s) exitosamente.")
            else:
                print("No se encontró ningún registro para actualizar.")

    except Error as e:
        print("Error al conectar con MySQL", e)

    finally:
        if cursor:
            cursor.close()
        if cnx and cnx.is_connected():
            cnx.close()