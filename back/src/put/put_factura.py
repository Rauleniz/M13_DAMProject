from flask import Blueprint, jsonify, request
from back.db import get_database_connection

actualizar_factura_bp = Blueprint('factura_put', __name__)

@actualizar_factura_bp.route('/factura/<int:factura_id>', methods=['PUT'])
def actualizar_factura(factura_id):
    try:
        # Obtener los datos de la factura del cuerpo de la solicitud
        data = request.json
        id_usuario = data.get('id_usuario')
        id_plan = data.get('id_plan')
        fecha_servicio = data.get('fecha_servicio')
        token_ahorro = data.get('token_ahorro')
        documentos = data.get('documentos')

        # Conectar a la base de datos
        connection = get_database_connection()
        
        cursor = connection.cursor()
        cursor.execute("UPDATE factura SET id_usuario = %s, id_plan = %s, fecha_servicio = %s, token_ahorro = %s, documentos = %s WHERE id = %s",
                       (id_usuario, id_plan, fecha_servicio, token_ahorro, documentos, factura_id))
        connection.commit()

        # Verificar si la factura se ha actualizado correctamente
        if cursor.rowcount > 0:
            return jsonify({'mensaje': 'Factura actualizada correctamente'}), 200
        else:
            return jsonify({'mensaje': 'La factura no se encontró o no se actualizó'}), 404

    except Exception as e:
        return jsonify({'mensaje': f"Error al actualizar la factura: {str(e)}"}), 500
