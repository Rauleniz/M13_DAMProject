"""
Middelware - Script para generar token de autenticación y posteriormente utilizarlo en el resto de scripts
"""

from functools import wraps
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/usuario', methods=['GET'])
@verificar_token
def obtener_usuario(id_usuario):
    # Lógica para obtener los datos del usuario
    datos_usuario = obtener_datos_usuario(id_usuario) # hay que definir la función en otro lugar del código
    return jsonify(datos_usuario)
