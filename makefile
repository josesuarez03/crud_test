VENV = venv
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip
TEST_DIR = test
URL = http://127.0.0.1:5000

# Crear entorno virtual y activar
$(VENV)/bin/activate: requirements.txt
	@echo "Creando entorno virtual..."
	python3 -m venv $(VENV)
	@echo "Instalando dependencias..."
	$(PIP) install -r requirements.txt

# Ejecutar la aplicación
run-app: $(VENV)/bin/activate
	@echo "Ejecutando la aplicación..."
	$(PYTHON) app.py

# Ejecutar todas las pruebas con separación de tiempo
test: $(VENV)/bin/activate
	@echo "Ejecutando pruebas unitarias..."
	$(PYTHON) -m unittest discover -s $(TEST_DIR) -p "testUnitarias.py"
	@echo "Esperando 5 segundos antes de la siguiente prueba..."
	sleep 5
	@echo "Ejecutando pruebas funcionales..."
	$(PYTHON) -m unittest discover -s $(TEST_DIR) -p "testFuncional.py"
	@echo "Esperando 5 segundos antes de la siguiente prueba..."
	sleep 5
	@echo "Ejecutando pruebas de integración..."
	$(PYTHON) -m unittest discover -s $(TEST_DIR) -p "testIntegracion.py"
	@echo "Esperando 5 segundos antes de la siguiente prueba..."
	sleep 5
	@echo "Ejecutando pruebas de seguridad..."
	$(PYTHON) -m unittest discover -s $(TEST_DIR) -p "testSeguridad.py"
	@echo "Esperando 5 segundos antes de la siguiente prueba..."
	sleep 5
	@echo "Ejecutando pruebas de rendimiento..."
	locust -f $(TEST_DIR)/testRendimiento.py --host=$(URL)


# Limpiar archivos generados
clean:
	@echo "Limpiando archivos generados..."
	rm -rf __pycache__
	rm -rf $(VENV)

