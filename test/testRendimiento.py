from locust import HttpUser, task, between

class ApiUser(HttpUser):
    # Tiempo de espera entre tareas (simula usuarios reales con pausas)
    wait_time = between(1, 5)

    # Escenario de prueba: Crear una cabra
    @task(1)
    def crear_cabra(self):
        self.client.post("/cabra", json={
            'nombre': 'Locust Test',
            'edad': 3,
            'raza': 'Boer',
            'color': 'Blanco',
            'peso': 50.5,
            'altura': 1.2,
            'produce_leche': True
        })

    # Escenario de prueba: Obtener la lista de cabras
    @task(2)
    def obtener_cabras(self):
        self.client.get("/cabra")

    # Escenario de prueba: Obtener una cabra específica
    @task(1)
    def obtener_cabra(self):
        # Este valor debería ser ajustado o extraído de datos previos
        cabra_id = 1
        self.client.get(f"/cabra/{cabra_id}")

    # Escenario de prueba: Actualizar una cabra
    @task(1)
    def actualizar_cabra(self):
        cabra_id = 1
        self.client.put(f"/cabra/{cabra_id}", json={
            'nombre': 'Locust Updated',
            'edad': 4,
            'raza': 'Angora',
            'color': 'Marrón',
            'peso': 55.0,
            'altura': 1.3,
            'produce_leche': False
        })

    # Escenario de prueba: Eliminar una cabra
    @task(1)
    def eliminar_cabra(self):
        cabra_id = 1
        self.client.delete(f"/cabra/{cabra_id}")
