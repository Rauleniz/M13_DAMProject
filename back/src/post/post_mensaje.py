from flask import Blueprint, request, jsonify
from datetime import datetime
from back.db import get_database_connection
from flask_socketio import send
from socketio_config import socketio

escribir_mensaje_bp = Blueprint('escribir_mensaje', __name__)

@escribir_mensaje_bp.route('/mensaje/escribir', methods=['POST'])
def escribir_mensaje():
    try:
        # Obtener los datos del mensaje del cuerpo de la solicitud
        data = request.json
        id_conversacion = data.get('id_conversacion')
        id_usuario = data.get('id_usuario')
        contenido = data.get('contenido')
        
        # Verificar si la conversación existe y si el usuario pertenece a ella
        connection = get_database_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM conversacion WHERE id = %s AND (id_usuario1 = %s OR id_usuario2 = %s)", (id_conversacion, id_usuario, id_usuario))
        conversacion = cursor.fetchone()
        if conversacion:
            # La conversación existe y el usuario pertenece a ella, podemos agregar el mensaje
            fecha_envio = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            cursor.execute("INSERT INTO mensaje (id_conversacion, id_usuario, contenido, fecha_envio) VALUES (%s, %s, %s, %s)", (id_conversacion, id_usuario, contenido, fecha_envio))
            connection.commit()
            connection.close()
            return jsonify({'mensaje': 'Mensaje enviado correctamente'}), 200
        else:
            return jsonify({'mensaje': 'Conversación no encontrada o el usuario no tiene permiso para enviar mensajes en esta conversación'}), 404
    except Exception as e:
        print(f"Error al escribir mensaje: {e}")
        return jsonify({'mensaje': 'Se produjo un error al escribir el mensaje'}), 500


@socketio.on('message')  # Usar la instancia de SocketIO
def handle_message(data):
    print('received message: ' + data)
    send(data, broadcast=True)