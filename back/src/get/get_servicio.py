from flask import Blueprint, current_app, jsonify, request
import jwt
from back.db import get_database_connection

get_servicio_bp = Blueprint('get_servicio', __name__)

@get_servicio_bp.route('/servicio/<int:usuario_id>', methods=['GET'])
def obtener_servicios(usuario_id):
    
    auth_header = request.headers.get('Authorization')
    if auth_header:
        token = auth_header.split(" ")[1]
    else:
        return jsonify({'mensaje': 'Token no proporcionado'}), 401

    try:
        data = jwt.decode(token,  current_app.config['SECRET_KEY'], algorithms=['HS256'])
        usuario_id = data['sub']
        # Conectar a la base de datos
        connection = get_database_connection()

        if connection:          
            cursor = connection.cursor()
            cursor.execute("SELECT * " \
                            "FROM servicio" \
                            "INNER JOIN plan_servicio ON servicio.id = plan_servicio.id_servicio" \
                            "INNER JOIN plan ON plan.id = plan_servicio.id_plan" \
                            "INNER JOIN usuario ON usuario.id_plan = plan.id" \
                            "WHERE usuario.id = %s", (usuario_id,))

            servicios = cursor.fetchall()

            # Verificar si se encontraron servicios
            if servicios:
                return jsonify(servicios), 200
            else:
                return jsonify({'mensaje': 'No se encontraron servicios'}), 404        
        else:
            return jsonify({'mensaje': 'Error de conexión a la base de datos'}), 500
    
    except Exception as e:
        return jsonify({'mensaje': f"Error al obtener los servicios: {str(e)}"}), 500

@get_servicio_bp.route('/servicio/<int:usuario_id>', methods=['OPTIONS'])
def options_usuario(usuario_id):
    return jsonify({'mensaje': 'OK'}), 200