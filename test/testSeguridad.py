import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
import json
from app import app, db, Cabra

class TestSeguridadAPI(unittest.TestCase):

    # Configuración inicial
    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # Base de datos en memoria para pruebas
        self.client = app.test_client()  # Cliente de prueba
        self.ctx = app.app_context()  # Crear un contexto de aplicación
        self.ctx.push()
        db.create_all()  # Crear las tablas de la base de datos

    # Limpiar después de cada prueba
    def tearDown(self):
        db.session.remove()  # Eliminar la sesión
        db.drop_all()  # Eliminar todas las tablas
        self.ctx.pop()  # Finalizar el contexto de la aplicación

    # 1. Test de inyección SQL en la creación de una cabra
    def test_inyeccion_sql(self):
        # Intentar inyección SQL en el nombre
        cabra_data = {
            'nombre': "'; DROP TABLE cabra;--",
            'edad': 3,
            'raza': 'Boer',
            'color': 'Blanco',
            'peso': 50.5,
            'altura': 1.2,
            'produce_leche': True
        }
        response = self.client.post('/cabra', data=json.dumps(cabra_data), content_type='application/json')
        
        # La API debe rechazar la inyección o manejarla sin dañar la base de datos
        self.assertNotEqual(response.status_code, 500)  # No debe dar un error del servidor
        self.assertEqual(response.status_code, 201)  # La solicitud debe funcionar correctamente

        # Verificar que la tabla 'cabra' sigue existiendo y no ha sido eliminada
        cabras = Cabra.query.all()
        self.assertGreater(len(cabras), 0)  # Debe existir al menos una cabra (la creada)

    # 2. Test de validación de entrada maliciosa en el campo numérico (edad negativa)
    def test_entrada_invalida_edad_negativa(self):
        # Intentar crear una cabra con edad negativa
        cabra_data = {
            'nombre': 'Cabra Maliciosa',
            'edad': -5,  # Edad negativa
            'raza': 'Boer',
            'color': 'Negro',
            'peso': 60.0,
            'altura': 1.1,
            'produce_leche': False
        }
        response = self.client.post('/cabra', data=json.dumps(cabra_data), content_type='application/json')

        # Esperar un error de cliente (400 Bad Request o similar)
        self.assertEqual(response.status_code, 400)  # Asegurarse que la entrada inválida es rechazada

    # 3. Test de validación de datos faltantes (campo obligatorio 'nombre' faltante)
    def test_entrada_faltante_nombre(self):
        # Intentar crear una cabra sin el nombre (dato requerido)
        cabra_data = {
            'edad': 3,
            'raza': 'Boer',
            'color': 'Blanco',
            'peso': 50.5,
            'altura': 1.2,
            'produce_leche': True
        }
        response = self.client.post('/cabra', data=json.dumps(cabra_data), content_type='application/json')

        # La solicitud debe fallar debido a la falta del campo obligatorio 'nombre'
        self.assertEqual(response.status_code, 400)  # Asegurar que devuelve un error 400

    # 4. Test para verificar que los errores
