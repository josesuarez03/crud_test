import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
import json
from app import app, db, Cabra

class TestCabraAPI(unittest.TestCase):

    # Configuración inicial de las pruebas
    def setUp(self):
        # Configurar el entorno de prueba
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # Base de datos en memoria para pruebas
        self.app = app.test_client()  # Cliente de pruebas
        self.ctx = app.app_context()  # Crear un contexto de aplicación
        self.ctx.push()  # Empujar el contexto
        db.create_all()  # Crear todas las tablas necesarias en la base de datos de pruebas

    # Limpiar después de cada prueba
    def tearDown(self):
        db.session.remove()  # Eliminar la sesión
        db.drop_all()  # Eliminar todas las tablas
        self.ctx.pop()  # Eliminar el contexto de la aplicación

    # Prueba para la creación de una cabra (POST)
    def test_crear_cabra(self):
        cabra_data = {
            'nombre': 'Lola',
            'edad': 3,
            'raza': 'Boer',
            'color': 'Blanco',
            'peso': 50.5,
            'altura': 1.2,
            'produce_leche': True
        }
        response = self.app.post('/cabra', data=json.dumps(cabra_data), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertIn('Lola', str(response.data))

    # Prueba para obtener todas las cabras (GET)
    def test_obtener_cabras(self):
        # Primero crear una cabra para que haya datos que obtener
        cabra = Cabra(nombre='Lola', edad=3, raza='Boer', color='Blanco', peso=50.5, altura=1.2, produce_leche=True)
        db.session.add(cabra)
        db.session.commit()

        # Luego hacer la solicitud GET para obtener las cabras
        response = self.app.get('/cabra')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['nombre'], 'Lola')

    # Prueba para obtener una cabra por ID (GET)
    def test_obtener_cabra_por_id(self):
        cabra = Cabra(nombre='Lola', edad=3, raza='Boer', color='Blanco', peso=50.5, altura=1.2, produce_leche=True)
        db.session.add(cabra)
        db.session.commit()

        response = self.app.get(f'/cabra/{cabra.id}')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['nombre'], 'Lola')

    # Prueba para actualizar una cabra (PUT)
    def test_actualizar_cabra(self):
        cabra = Cabra(nombre='Lola', edad=3, raza='Boer', color='Blanco', peso=50.5, altura=1.2, produce_leche=True)
        db.session.add(cabra)
        db.session.commit()

        nueva_data = {
            'nombre': 'Lola Actualizada',
            'edad': 4,
            'raza': 'Angora',
            'color': 'Marrón',
            'peso': 55.0,
            'altura': 1.3,
            'produce_leche': False
        }
        response = self.app.put(f'/cabra/{cabra.id}', data=json.dumps(nueva_data), content_type='application/json')
        self.assertEqual(response.status_code, 200)

        # Verificar si la cabra fue actualizada
        cabra_actualizada = Cabra.query.get(cabra.id)
        self.assertEqual(cabra_actualizada.nombre, 'Lola Actualizada')
        self.assertEqual(cabra_actualizada.edad, 4)

    # Prueba para eliminar una cabra (DELETE)
    def test_eliminar_cabra(self):
        cabra = Cabra(nombre='Lola', edad=3, raza='Boer', color='Blanco', peso=50.5, altura=1.2, produce_leche=True)
        db.session.add(cabra)
        db.session.commit()

        response = self.app.delete(f'/cabra/{cabra.id}')
        self.assertEqual(response.status_code, 200)
        self.assertIn(f'La cabra con ID {cabra.id} ha sido eliminada.', str(response.data))

        # Verificar si la cabra fue eliminada
        cabra_eliminada = Cabra.query.get(cabra.id)
        self.assertIsNone(cabra_eliminada)

if __name__ == '__main__':
    unittest.main()
