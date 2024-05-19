from flask import Blueprint, jsonify, request
from back.db import get_database_connection

#con archivo de audio:
from werkzeug.utils import secure_filename
import os

post_ubicacion_bp = Blueprint('post_ubicacion', __name__)

@post_ubicacion_bp.route('/ubicacion', methods=['POST'])
def agregar_ubicacion():
    try:

        # Acceder al archivo de audio
        audio_file = request.files['audioFile']
        # Asegurar que el nombre del archivo es seguro
        secure_filename(audio_file.filename)
        # Guardar el archivo de audio en el servidor
        audio_file.save(os.path.join('ruta/donde/guardar/el/archivo', audio_file.filename))

        

        # Obtener los datos de la solicitud
        data = request.json
        id_usuario = data.get('usuario_id')
        lat = data.get('lat')
        lng = data.get('lng')
        descripcion = data.get('descripcion')
        link1 = data.get('link1')
        link2 = data.get('link2')
        link3 = data.get('link3')
        link4 = data.get('link4')

        # Conectar a la base de datos
        connection = get_database_connection()
        cursor = connection.cursor()

        # Insertar la ubicación en la tabla de ubicaciones
        cursor.execute("INSERT INTO ubicacion (id_usuario, lat, lng, descripcion, link1, link2, link3, link4) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                       (id_usuario, lat, lng, descripcion, link1, link2, link3, link4))
        connection.commit()

        # Verificar si la ubicación se ha insertado correctamente
        if cursor.rowcount > 0:
            return jsonify({'mensaje': 'Ubicación agregada correctamente'}), 201
        else:
            return jsonify({'mensaje': 'Error al agregar la ubicación'}), 500

    except Exception as e:
        return jsonify({'mensaje': f"Error al agregar la ubicación: {str(e)}"}), 500
