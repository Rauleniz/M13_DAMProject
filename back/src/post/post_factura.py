from flask import Blueprint, jsonify, request
from back.db import get_database_connection

crear_factura_bp = Blueprint('factura_post', __name__)

@crear_factura_bp.route('/factura', methods=['POST'])
def crear_factura():
    try:        
        data = request.json
        id_usuario = data.get('id_usuario')
        id_plan = data.get('id_plan')
        fecha_servicio = data.get('fecha_servicio')
        token_ahorro = data.get('token_ahorro')
        documentos = data.get('documentos')

        connection = get_database_connection()

        # Insertar la nueva factura en la base de datos
        cursor = connection.cursor()
        cursor.execute("INSERT INTO factura (id_usuario, id_plan, fecha_servicio, token_ahorro, documentos) VALUES (%s, %s, %s, %s, %s)",
                       (id_usuario, id_plan, fecha_servicio, token_ahorro, documentos))
        connection.commit()

        # Verificar si la factura se ha insertado correctamente
        if cursor.rowcount > 0:
            return jsonify({'mensaje': 'Factura creada correctamente'}), 201
        else:
            return jsonify({'mensaje': 'Error al crear la factura'}), 500

    except Exception as e:
        return jsonify({'mensaje': f"Error al crear la factura: {str(e)}"}), 500
