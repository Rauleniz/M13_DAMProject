from flask import Blueprint, current_app, request, jsonify
from datetime import datetime
import jwt
from back.db import get_database_connection
from flask_socketio import send
from socketio_config import socketio

escribir_mensaje_bp = Blueprint('escribir_mensaje', __name__)

@escribir_mensaje_bp.route('/mensaje/escribir/<int:usuario_id>', methods=['POST'])
def escribir_mensaje(usuario_id):

    auth_header = request.headers.get('Authorization')
    if auth_header:
        token = auth_header.split(" ")[1]
    else:
        return jsonify({'mensaje': 'Token no proporcionado'}), 401

    try:
        data_token = jwt.decode(token,  current_app.config['SECRET_KEY'], algorithms=['HS256'])
        usuario_id = data_token['sub']      
        data = request.json
        id_conversacion = data.get('id_conversacion')
        id_usuario = data.get('id_usuario')
        contenido = data.get('contenido')
        
        # Si la conversación existe y el usuario pertenece a ella, se agrega el mensaje
        connection = get_database_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM conversacion WHERE id = %s AND (id_usuario1 = %s OR id_usuario2 = %s)", (id_conversacion, usuario_id, id_usuario))
        conversacion = cursor.fetchone()
        if conversacion:            
            fecha_envio = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            cursor.execute("INSERT INTO mensaje (id_conversacion, id_usuario, contenido, fecha_envio) VALUES (%s, %s, %s, %s)", (id_conversacion, usuario_id, contenido, fecha_envio))
            connection.commit()
            connection.close()
            return jsonify({'mensaje': 'Mensaje enviado correctamente'}), 200
        else:
            return jsonify({'mensaje': 'Conversación no encontrada o el usuario no tiene permiso para enviar mensajes en esta conversación'}), 404
    except Exception as e:
        print(f"Error al escribir mensaje: {e}")
        return jsonify({'mensaje': 'Se produjo un error al escribir el mensaje'}), 500


@socketio.on('message')
def handle_message(data):
    print('received message: ' + data['contenido'])
    send(data, broadcast=True)

@escribir_mensaje_bp.route('/mensaje/escribir/<int:usuario_id>', methods=['OPTIONS'])
def options_usuario(usuario_id):
    return jsonify({'mensaje': 'OK'}), 200