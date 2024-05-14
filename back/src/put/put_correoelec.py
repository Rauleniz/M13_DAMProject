"""
Script de prueba. en verda
"""


from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from back.db import get_database_connection

put_correo_bp = Blueprint('correo_put', __name__)


# Ruta para actualizar el correo electrónico del usuario
@put_correo_bp.route('/usuario/email', methods=['PATCH'])
@jwt_required()  # Verificar que el token JWT sea válido
def actualizar_email():
    try:
        # Obtener el ID del usuario del token JWT
        usuario_id = get_jwt_identity()

        # Obtener el ID del usuario del cuerpo de la solicitud JSON
        usuario_actualizar_id = request.json.get('id')

        # Verificar que el usuario que está intentando actualizar el correo electrónico sea el mismo que está autenticado en el token
        if usuario_actualizar_id != usuario_id:
            return jsonify({'mensaje': 'No estás autorizado para realizar esta acción'}), 403

        # Obtener el nuevo correo electrónico del cuerpo de la solicitud
        nuevo_email = request.json.get('email')

        # Actualizar el correo electrónico del usuario en la base de datos
        connection = get_database_connection()
        if connection:
            with connection.cursor() as cursor:
                sql = "UPDATE usuario SET email = %s WHERE id = %s"
                cursor.execute(sql, (nuevo_email, usuario_id))
                connection.commit()
                return jsonify({'mensaje': 'Correo electrónico actualizado correctamente'}), 200
        else:
            return jsonify({'mensaje': 'Error al conectar a la base de datos'}), 500
    except Exception as e:
        print("Error al actualizar el correo electrónico:", e)
        return jsonify({'mensaje': 'Error interno del servidor'}), 500