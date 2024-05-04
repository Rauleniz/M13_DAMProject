from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255))
    apellidos = db.Column(db.String(255))
    email = db.Column(db.String(255))
    direccion = db.Column(db.String(255))
    descripcion = db.Column(db.String(255))
    estatus = db.Column(db.String(255))
    img_perfil = db.Column(db.String(255))
    cancion = db.Column(db.String(255))
    id_plan = db.Column(db.Integer)
    link_rrss = db.Column(db.String(255))
    username = db.Column(db.String(255))
    password = db.Column(db.String(255))

    def to_json(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "apellidos": self.apellidos,
            "email": self.email,
            "direccion": self.direccion,
            "descripcion": self.descripcion,
            "estatus": self.estatus,
            "img_perfil": self.img_perfil,
            "cancion": self.cancion,
            "id_plan": self.id_plan,
            "link_rrss": self.link_rrss,
            "username": self.username,
            "password": self.password
        }

class Conversacion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_usuario1 = db.Column(db.Integer)
    id_usuario2 = db.Column(db.Integer)
    ultima_actividad = db.Column(db.TIMESTAMP)

    def to_json(self):
        return {
            "id": self.id,
            "id_usuario1": self.id_usuario1,
            "id_usuario2": self.id_usuario2,
            "ultima_actividad": self.ultima_actividad
        }

class Mensaje(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_conversacion = db.Column(db.Integer)
    id_usuario = db.Column(db.Integer)
    contenido = db.Column(db.String(255))
    fecha_envio = db.Column(db.TIMESTAMP)

    def to_json(self):
        return {
            "id": self.id,
            "id_conversacion": self.id_conversacion,
            "id_usuario": self.id_usuario,
            "contenido": self.contenido,
            "fecha_envio": self.fecha_envio
        }

class DatosBancarios(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer)
    id_factura = db.Column(db.Integer)
    nombre_iban = db.Column(db.String(255))
    numero_tarjeta = db.Column(db.String(255))
    caducidad_tarjeta = db.Column(db.String(255))
    cvc = db.Column(db.String(255))

    def to_json(self):
        return {
            "id": self.id,
            "id_usuario": self.id_usuario,
            "id_factura": self.id_factura,
            "nombre_iban": self.nombre_iban,
            "numero_tarjeta": self.numero_tarjeta,
            "caducidad_tarjeta": self.caducidad_tarjeta,
            "cvc": self.cvc
        }

class Multimedia(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer)
    img = db.Column(db.String(255))
    song = db.Column(db.String(255))

    def to_json(self):
        return {
            "id": self.id,
            "id_usuario": self.id_usuario,
            "img": self.img,
            "song": self.song
        }


class Factura(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer)
    id_plan = db.Column(db.Integer)
    fecha_servicio = db.Column(db.TIMESTAMP)
    token_ahorro = db.Column(db.Float)
    documentos = db.Column(db.String(255))

    def to_json(self):
        return {
            "id": self.id,
            "id_usuario": self.id_usuario,
            "id_plan": self.id_plan,
            "fecha_servicio": self.fecha_servicio,
            "token_ahorro": self.token_ahorro,
            "documentos": self.documentos
        }

class Plan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255))
    cambio_plan = db.Column(db.String(255))

    def to_json(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "cambio_plan": self.cambio_plan
        }


class Servicio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    asignacion_tecnico = db.Column(db.String(255))
    cheque = db.Column(db.String(255))
    financiacion = db.Column(db.String(255))
    seguro = db.Column(db.String(255))
    alquiler_furgon = db.Column(db.String(255))

    def to_json(self):
        return {
            "id": self.id,
            "asignacion_tecnico": self.asignacion_tecnico,
            "cheque": self.cheque,
            "financiacion": self.financiacion,
            "seguro": self.seguro,
            "alquiler_furgon": self.alquiler_furgon
        }

class PlanServicio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_plan = db.Column(db.Integer)
    id_servicio = db.Column(db.Integer)

    def to_json(self):
        return {
            "id": self.id,
            "id_plan": self.id_plan,
            "id_servicio": self.id_servicio
        }

class Ubicacion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer)
    latitud = db.Column(db.Float)
    longitud = db.Column(db.Float)
    direccion = db.Column(db.String(255))

    def to_json(self):
        return {
            "id": self.id,
            "id_usuario": self.id_usuario,
            "latitud": self.latitud,
            "longitud": self.longitud,
            "direccion": self.direccion
        }


# Intentar inicializar la base de datos
def init_db(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()