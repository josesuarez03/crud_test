VENV = venv
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip
TEST_DIR = test

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

# Ejecutar todas las pruebas
test: $(VENV)/bin/activate
	@echo "Ejecutando pruebas unitarias..."
	$(PYTHON) $(TEST_DIR)/testUnitarias.py
	@echo "Ejecutando pruebas funcionales..."
	$(PYTHON) $(TEST_DIR)/testFuncional.py
	@echo "Ejecutando pruebas de integración..."
	$(PYTHON) $(TEST_DIR)/testIntegracion.py
	@echo "Ejecutando pruebas de rendimiento..."
	$(PYTHON) $(TEST_DIR)/testRendimiento.py
	@echo "Ejecutando pruebas de seguridad..."
	$(PYTHON) $(TEST_DIR)/testSeguridad.py

# Limpiar archivos generados
clean:
	@echo "Limpiando archivos generados..."
	rm -rf __pycache__
	rm -rf $(VENV)
