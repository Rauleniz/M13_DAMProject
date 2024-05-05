from flask import Blueprint, jsonify
from back.db import get_database_connection

get_factura_usuario_bp = Blueprint('factura_usuario_get', __name__)

@get_factura_usuario_bp.route('/factura/<int:id_usuario>', methods=['GET'])
def obtener_factura_usuario(id_usuario):
    try:
        # Conectar a la base de datos
        connection = get_database_connection()

        # Obtener las facturas del usuario especificado
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM factura WHERE id_usuario = %s", (id_usuario,))
        facturas = cursor.fetchall()

        # Verificar si se encontraron facturas para el usuario
        if facturas:
            return jsonify(facturas), 200
        else:
            return jsonify({'mensaje': 'No se encontraron facturas para el usuario especificado'}), 404

    except Exception as e:
        return jsonify({'mensaje': f"Error al obtener las facturas del usuario: {str(e)}"}), 500
