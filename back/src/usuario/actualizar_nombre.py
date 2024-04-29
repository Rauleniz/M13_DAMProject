from flask import Blueprint, request, jsonify, current_app
from back.db import get_database_connection
from auth import verificar_credenciales_decorador

actualizar_nombre_bp = Blueprint('actualizar_nombre', __name__)

def actualizar_nombre_en_db(usuario_id, nuevo_nombre):
    try:
        # Establecer conexión con la base de datos
        connection = get_database_connection()

        # Preparar y ejecutar la consulta SQL para actualizar el nombre del usuario
        sql = "UPDATE usuario SET nombre = %s WHERE id = %s"
        with connection.cursor() as cursor:
            cursor.execute(sql, (nuevo_nombre, usuario_id))
        
        # Confirmar los cambios en la base de datos
        connection.commit()

        # Cerrar la conexión con la base de datos
        connection.close()

        return True
    except Exception as e:
        current_app.logger.error("Error al actualizar el nombre en la base de datos: %s", str(e))
        return False
    

@actualizar_nombre_bp.route('/usuario/actualizar/nombre', methods=['PATCH'])
@verificar_credenciales_decorador
def actualizar_nombre(usuario):
    try:
        # Obtener el nuevo nombre del usuario del cuerpo de la solicitud
        nuevo_nombre = request.json.get('nombre')

        # Aquí va el código para actualizar el nombre del usuario en la base de datos
        # Supongamos que hay una función actualizar_nombre_en_db(nombre, usuario_id)

        actualizar_nombre_en_db(nuevo_nombre, usuario['id'])

        # Respuesta de éxito
        return jsonify({'mensaje': 'Nombre actualizado correctamente'}), 200
    except Exception as e:
        # Manejo de errores
        return jsonify({'mensaje': 'Error al actualizar el nombre', 'error': str(e)}), 500
