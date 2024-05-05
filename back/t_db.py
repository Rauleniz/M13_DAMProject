import mysql.connector
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
rutas = ["http://localhost:5500", "http://127.0.0.1:5500"]
CORS(app, supports_credentials=True, allow_headers=["Content-Type", "Authorization"], resources={r"/*": {"origins": rutas}}, methods=["GET", "POST", "PATCH", "DELETE", "OPTIONS"])

app.config['CORS_LOGGING'] = True

app.config['SECRET_KEY'] = 'DamM13&Proj3ct'

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/m13db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Suprime la señalización de modificaciones de la base de datos

db = SQLAlchemy(app)

