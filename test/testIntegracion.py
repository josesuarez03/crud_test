import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
import json
from app import app, db, Cabra

class TestIntegracionAPI(unittest.TestCase):

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

    # Test de integración completo
    def test_integracion_crud(self):
        # 1. Crear una nueva cabra (POST)
        cabra_data = {
            'nombre': 'Lola',
            'edad': 3,
            'raza': 'Boer',
            'color': 'Blanco',
            'peso': 50.5,
            'altura': 1.2,
            'produce_leche': True
        }
        response = self.client.post('/cabra', data=json.dumps(cabra_data), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        cabra_creada = json.loads(response.data)
        self.assertEqual(cabra_creada['nombre'], 'Lola')

        cabra_id = cabra_creada['id']  # Guardar el ID de la cabra creada para usarlo después

        # 2. Obtener la cabra creada (GET)
        response = self.client.get(f'/cabra/{cabra_id}')
        self.assertEqual(response.status_code, 200)
        cabra_obtenida = json.loads(response.data)
        self.assertEqual(cabra_obtenida['nombre'], 'Lola')
        self.assertEqual(cabra_obtenida['edad'], 3)

        # 3. Actualizar la cabra (PUT)
        nueva_data = {
            'nombre': 'Lola Actualizada',
            'edad': 4,
            'raza': 'Angora',
            'color': 'Marrón',
            'peso': 55.0,
            'altura': 1.3,
            'produce_leche': False
        }
        response = self.client.put(f'/cabra/{cabra_id}', data=json.dumps(nueva_data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        cabra_actualizada = json.loads(response.data)
        self.assertEqual(cabra_actualizada['nombre'], 'Lola Actualizada')
        self.assertEqual(cabra_actualizada['edad'], 4)

        # 4. Verificar que los cambios han sido aplicados (GET actualizado)
        response = self.client.get(f'/cabra/{cabra_id}')
        self.assertEqual(response.status_code, 200)
        cabra_obtenida_actualizada = json.loads(response.data)
        self.assertEqual(cabra_obtenida_actualizada['nombre'], 'Lola Actualizada')
        self.assertEqual(cabra_obtenida_actualizada['raza'], 'Angora')
        self.assertEqual(cabra_obtenida_actualizada['produce_leche'], False)

        # 5. Eliminar la cabra (DELETE)
        response = self.client.delete(f'/cabra/{cabra_id}')
        self.assertEqual(response.status_code, 200)
        self.assertIn(f"La cabra con ID {cabra_id} ha sido eliminada.", str(response.data))

        # 6. Verificar que la cabra ha sido eliminada (GET debería dar 404)
        response = self.client.get(f'/cabra/{cabra_id}')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()
