from flask import Blueprint, jsonify
from back.src.get.get_usuario import get_usuarios_bp
from back.src.put.put_usuario import put_usuarios_bp
from back.src.post.post_usuario import post_usuarios_bp
from back.src.get.get_plan import get_plan_bp
from back.src.post.post_bancario import post_bancarios_bp
from back.src.usuario.actualizar_nombre import actualizar_nombre_bp
from back.src.get.info_usuario import usuario_info_bp


def register_endpoints(app):
    app.register_blueprint(get_usuarios_bp, url_prefix='/get')   
    app.register_blueprint(put_usuarios_bp, url_prefix='/put')
    app.register_blueprint(post_usuarios_bp, url_prefix='/post')
    app.register_blueprint(get_plan_bp, url_prefix='/get')
    app.register_blueprint(post_bancarios_bp, url_prefix='/post')
    app.register_blueprint(actualizar_nombre_bp, url_prefix='/usuario')
    app.register_blueprint(usuario_info_bp, url_prefix='/get')
