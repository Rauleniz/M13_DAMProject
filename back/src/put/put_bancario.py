from flask import Blueprint, jsonify, request, session
from back.auth import verificar_credenciales_decorador
from back.db import get_database_connection

put_bancarios_bp = Blueprint('bancarios_put', __name__)

@put_bancarios_bp.route('/bancario', methods=['PUT'])
@verificar_credenciales_decorador
def actualizar_datos_bancarios():
    connection = get_database_connection()

    try:
        # Verificar si el usuario está autenticado y obtener su ID de la sesión
        if 'user_id' not in session:
            return jsonify({'mensaje': 'Usuario no autenticado'}), 401
        user_id = session['user_id']

        data = request.json
        nombre_tarjeta = data.get('nombre_tarjeta')
        numero_tarjeta = data.get('numero_tarjeta')
        caducidad_tarjeta = data.get('caducidad_tarjeta')
        cvc = data.get('cvc')

        cursor = connection.cursor()
        sql = "UPDATE datosbancarios SET nombre_tarjeta = %s, numero_tarjeta = %s, caducidad_tarjeta = %s, cvc = %s WHERE id_usuario = %s"
        cursor.execute(sql, (nombre_tarjeta, numero_tarjeta, caducidad_tarjeta, cvc, user_id))
        connection.commit()

        if cursor.rowcount > 0:
            return jsonify({'mensaje': 'Datos bancarios actualizados correctamente'})
        else:
            return jsonify({'mensaje': 'Error. No se han actualizado los datos bancarios'}), 404
    except Exception as e:
        print(f"Error al actualizar los datos bancarios: {e}")
        return jsonify({'mensaje': 'Se produjo un error al actualizar los datos bancarios'}), 500