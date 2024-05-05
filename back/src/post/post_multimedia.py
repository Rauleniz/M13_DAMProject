from flask import Blueprint, jsonify, request
from back.db import get_database_connection

post_multimedia_bp = Blueprint('multimedia_post', __name__)

@post_multimedia_bp.route('/multimedia', methods=['POST'])
def crear_multimedia():
    try:
        # Obtener los datos del multimedia del cuerpo de la solicitud
        data = request.json
        id_usuario = data.get('id_usuario')
        img = data.get('img')
        song = data.get('song')

        # Conectar a la base de datos
        connection = get_database_connection()
        cursor = connection.cursor()

        # Insertar multimedia en la base de datos
        cursor.execute("INSERT INTO multimedia (id_usuario, img, song) VALUES (%s, %s, %s)",
                       (id_usuario, img, song))
        connection.commit()

        # Verificar si el multimedia se ha insertado correctamente
        if cursor.rowcount > 0:
            return jsonify({'mensaje': 'Multimedia creado correctamente'}), 201
        else:
            return jsonify({'mensaje': 'Error al crear multimedia'}), 500

    except Exception as e:
        return jsonify({'mensaje': f"Error al crear multimedia: {str(e)}"}), 500
