import unittest

from flask import jsonify
from auth import verificar_credenciales, verificar_credenciales_decorador

class TestAuth(unittest.TestCase):
    def test_verificar_credenciales(self):
        # Prueba con credenciales válidas
        usuario_valido = verificar_credenciales('usuario', 'contraseña')
        self.assertIsNotNone(usuario_valido)
        
        # Prueba con credenciales inválidas
        usuario_invalido = verificar_credenciales('usuario', 'contraseña_incorrecta')
        self.assertIsNone(usuario_invalido)
        
    def test_verificar_credenciales_decorador(self):
        # Prueba con una función de prueba simulada
        @verificar_credenciales_decorador
        def funcion_prueba(usuario):
            return 'Hola, {}'.format(usuario['username'])
        
        # Prueba con credenciales válidas
        resultado_valido = funcion_prueba({'username': 'usuario', 'id': 1})
        self.assertEqual(resultado_valido, 'Hola, usuario')
        
        # Prueba con credenciales inválidas
        resultado_invalido = funcion_prueba(None)
        self.assertEqual(resultado_invalido, jsonify({'mensaje': '**/Credenciales incorrectas'}), 401)

if __name__ == '__main__':
    unittest.main()
