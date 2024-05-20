import os
from flask import Blueprint, current_app, jsonify, request
import jwt
from back.db import get_database_connection
from werkzeug.utils import secure_filename


actualizar_multimedia_bp = Blueprint('multimedia_put', __name__)

@actualizar_multimedia_bp.route('/multimedia/<int:usuario_id>', methods=['PUT'])
def actualizar_multimedia(usuario_id):

    auth_header = request.headers.get('Authorization')
    if auth_header:
        token = auth_header.split(" ")[1]
    else:
        return jsonify({'mensaje': 'Token no proporcionado'}), 401

    try:
        data = jwt.decode(token,  current_app.config['SECRET_KEY'], algorithms=['HS256'])
        usuario_id = data['sub']


        data_solictud = request.json
        img = data_solictud.get('tarjeta_img')
        song = data_solictud.get('tarjeta_song')

        # Acceder al archivo de audio
        audio_file = request.files['audioFile']
        # Asegurar que el nombre del archivo es seguro
        secure_filename(audio_file.filename)
        # Guardar el archivo de audio en el servidor
        audio_file.save(os.path.join('ruta/donde/guardar/el/archivo', audio_file.filename))

        # Conectar a la base de datos
        connection = get_database_connection()
        
        cursor = connection.cursor()
        cursor.execute("UPDATE multimedia SET img=%s, song=%s WHERE id=%s",
                       (img, song, usuario_id))
        connection.commit()

        # Verificar si se ha actualizado correctamente
        if cursor.rowcount > 0:
            return jsonify({'mensaje': 'Multimedia actualizado correctamente'}), 200
        else:
            return jsonify({'mensaje': 'Error al actualizar multimedia'}), 404

    except Exception as e:
        return jsonify({'mensaje': f"Error al actualizar multimedia: {str(e)}"}), 500

@actualizar_multimedia_bp.route('/usuario/<int:usuario_id>', methods=['OPTIONS'])
def options_usuario(usuario_id):
    return jsonify({'mensaje': 'OK'}), 200