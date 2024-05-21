from flask import Blueprint, jsonify, request
from back.db import get_database_connection
#con archivo de audio:
from werkzeug.utils import secure_filename
import os

post_multimedia_bp = Blueprint('multimedia_post', __name__)

@post_multimedia_bp.route('/multimedia/<int:usuario_id>', methods=['POST'])
def crear_multimedia(usuario_id):

    auth_header = request.headers.get('Authorization')
    if auth_header:
        token = auth_header.split(" ")[1]
    else:
        return jsonify({'mensaje': 'Token no proporcionado'}), 401    
      
    connection = get_database_connection()

    try:

        # Acceder al archivo de audio
        audio_file = request.files['audioFile']
        # Asegurar que el nombre del archivo es seguro
        secure_filename(audio_file.filename)
        # Guardar el archivo de audio en el servidor
        audio_file.save(os.path.join('ruta/donde/guardar/el/archivo', audio_file.filename))


        data = request.json
        img = data.get('tarjeta_img')
        song = data.get('tarjeta_song')

        cursor = connection.cursor()
      
        cursor.execute("INSERT INTO multimedia (id_usuario, img, song) VALUES (%s, %s, %s)",
                       (usuario_id, img, song))
        connection.commit()

        # Verificar si el multimedia se ha insertado correctamente
        if cursor.rowcount > 0:
            return jsonify({'mensaje': 'Multimedia creado correctamente'}), 201
        else:
            return jsonify({'mensaje': 'Error al crear multimedia'}), 500

    except Exception as e:
        return jsonify({'mensaje': f"Error al crear multimedia: {str(e)}"}), 500

@post_multimedia_bp.route('/multimedia/<int:usuario_id>', methods=['OPTIONS'])
def options_usuario(usuario_id):
    return jsonify({'mensaje': 'OK'}), 200