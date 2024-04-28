import mysql.connector

# Configuración de la conexión a la base de datos MySQL /// 3306
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'root',
    'database': 'm13db'
}

# Intentar conectar a la base de datos
def get_database_connection():
    try:
        connection = mysql.connector.connect(**db_config)
        if connection.is_connected():
            print('Conexión exitosa a la base de datos MySQL')
            return connection
        else:
            print('Error al conectar a la base de datos')
            return None
    except Exception as e:
        print('Error al conectar a la base de datos:', e)
        return None
