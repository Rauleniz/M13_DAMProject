from flask import Blueprint, jsonify, request
from back.db import get_database_connection
from app import app, db
from models import Usuario



@app.route('/usuarios', methods = ['GET'])
def get_usuarios():
    usuarios = Usuario.query.all()
    json_usuarios = list(map(lambda x: x.to_json(),usuarios))
    return jsonify({"usuarios": json_usuarios})


#del tuto, lo hace en el main.py. de momento lo hago en este script borrador
if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)