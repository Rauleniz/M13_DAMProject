from flask import Blueprint, jsonify, request
from back.db import get_database_connection

post_servicio_bp = Blueprint('post_servicio', __name__)

@post_servicio_bp.route('/servicio/<int:usuario_id>', methods=['POST'])
def agregar_servicio(usuario_id):
    try:
        data = request.json
        asignacion_tecnico = data.get('tarjeta_tecnico')
        cheque = data.get('tarjeta_cheque')
        financiacion = data.get('tarjeta_financiacion')
        seguro = data.get('tarjeta_seguro')
        alquiler_furgon = data.get('tarjeta_furgon')

        connection = get_database_connection()
        cursor = connection.cursor()

        cursor.execute("INSERT INTO servicio (asignacion_tecnico, cheque, financiacion, seguro, alquiler_furgon) VALUES (%s, %s, %s, %s, %s)",
                       (asignacion_tecnico, cheque, financiacion, seguro, alquiler_furgon))
        connection.commit()

        # Obtener el ID del servicio recién insertado
        servicio_id = cursor.lastrowid

        cursor.execute("INSERT INTO plan_servicio (id_plan, id_servicio) VALUES (%s, %s)",
                       (data.get('id_plan'), servicio_id))
        connection.commit()

        # Verificar si el servicio se ha insertado correctamente
        if cursor.rowcount > 0:
            return jsonify({'mensaje': 'Servicio agregado correctamente'}), 201
        else:
            return jsonify({'mensaje': 'Error al agregar el servicio'}), 500

    except Exception as e:
        return jsonify({'mensaje': f"Error al agregar el servicio: {str(e)}"}), 500

@post_servicio_bp.route('/servicio/<int:usuario_id>', methods=['OPTIONS'])
def options_usuario(usuario_id):
    return jsonify({'mensaje': 'OK'}), 200