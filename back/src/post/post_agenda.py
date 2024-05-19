from flask import Blueprint, current_app, jsonify, request, session
import jwt
from back.db import get_database_connection

post_agenda_bp = Blueprint('agenda_post', __name__)

@post_agenda_bp.route('/agenda/<int:usuario_id>', methods=['POST'])
def nuevo_evento_agenda(usuario_id):

    auth_header = request.headers.get('Authorization')
    if auth_header:
        token = auth_header.split(" ")[1]
    else:
        return jsonify({'mensaje': 'Token no proporcionado'}), 401


    connection = get_database_connection()

    try:    
        data_token = jwt.decode(token,  current_app.config['SECRET_KEY'], algorithms=['HS256'])
        usuario_id = data_token['sub']

        data_solicitud = request.json
        fecha = data_solicitud.get('agenda_fecha')
        titulo = data_solicitud.get('agenda_titulo')
        descripcion = data_solicitud.get('agenda_descripcion')
  
        cursor = connection.cursor()
        sql = "INSERT INTO agenda (id_usuario, fecha, titulo, descripcion) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (usuario_id, fecha, titulo, descripcion))
        connection.commit()

        if cursor.rowcount > 0:
            return jsonify({'mensaje': 'Evento dado de alta correctamente'})
        else:
            return jsonify({'mensaje': 'Error. No se ha guardado el Evento'}), 404
    except Exception as e:
        print(f"Error al crear el Evento: {e}")
        return jsonify({'mensaje': 'Se produjo un error al dar de alta el Evento'}), 500

@post_agenda_bp.route('/bancario/<int:id_usuario>', methods=['OPTIONS'])
def options_usuario(usuario_id):
    return jsonify({'mensaje': 'OK'}), 200