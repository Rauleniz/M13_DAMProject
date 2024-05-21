from flask import Blueprint, current_app, jsonify, request
import jwt
from back.db import get_database_connection

put_servicio_bp = Blueprint('put_servicio', __name__)

@put_servicio_bp.route('/servicio/<int:usuario_id>', methods=['PUT'])
def actualizar_servicio(usuario_id):

    auth_header = request.headers.get('Authorization')
    if auth_header:
        token = auth_header.split(" ")[1]
    else:
        return jsonify({'mensaje': 'Token no proporcionado'}), 401

    try:
        data = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=['HS256'])
        usuario_id = data['sub']
       
        data_solicitud = request.json
        asignacion_tecnico = data_solicitud.get('tarjeta_tecnico')
        cheque = data_solicitud.get('tarjeta_cheque')
        financiacion = data_solicitud.get('tarjeta_financiacion')
        seguro = data_solicitud.get('tarjeta_seguro')
        alquiler_furgon = data_solicitud.get('tarjeta_furgon')
      
        connection = get_database_connection()
        cursor = connection.cursor()

        cursor.execute("SELECT id_plan FROM usuario WHERE id = %s", (usuario_id,))
        id_plan = cursor.fetchone()[0]

        cursor.execute("SELECT id_servicio FROM plan_servicio WHERE id_plan = %s", (id_plan,))
        ids_servicio = [row[0] for row in cursor.fetchall()]

        # Actualizar el servicio en la base de datos
        for id_servicio in ids_servicio:
            sql = "UPDATE servicio SET "
            params = []
            for key, value in data_solicitud.items():
                sql += f"{key} = %s, "
                params.append(value)
            sql = sql.rstrip(', ')  # Eliminar la última coma
            sql += " WHERE id = %s"
            params.append(id_servicio)

            connection.commit()

        # Verificar si el servicio se ha actualizado correctamente
        if cursor.rowcount > 0:
            return jsonify({'mensaje': 'Servicio actualizado correctamente'}), 200
        else:
            return jsonify({'mensaje': 'Error al actualizar el servicio'}), 404

    except Exception as e:
        return jsonify({'mensaje': f"Error al actualizar el servicio: {str(e)}"}), 500

@put_servicio_bp.route('/servicio/<int:usuario_id>', methods=['OPTIONS'])
def options_usuario(usuario_id):
    return jsonify({'mensaje': 'OK'}), 200