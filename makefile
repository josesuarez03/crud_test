VENV = venv
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip
TEST_DIR = test
URL = http://127.0.0.1:5000
CURDIR = $(shell pwd)

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

pylint: $(VENV)/bin/activate
	@echo "Ejecutando pylint..."
	$(VENV)/bin/pylint $(CURDIR)/**/*.py
	sleep 2

coverage: $(VENV)/bin/activate
	@echo "Generando informe de cobertura..."
	$(PYTHON) -m coverage run --source=. -m unittest discover -s $(TEST_DIR)
	sleep 2
	$(PYTHON) -m coverage report -m
	sleep 2

# Trivy con ruta relativa
trivy: 
	@echo "Ejecutando análisis de seguridad con Trivy..."
	trivy fs $(CURDIR)

# Cifrar el archivo secrets.yaml
encrypt:
	@echo "Cifrando el archivo secrets.yaml..."
	@read -p "Introduce tu PGP Key ID (últimos 8 caracteres o ID completo): " PGP_KEY_ID; \
	sops --encrypt --pgp $$PGP_KEY_ID secrets.yaml > secrets.enc.yaml; \
	echo "Archivo cifrado como secrets.enc.yaml"

# Descifrar el archivo secrets.enc.yaml
decrypt:
	@echo "Descifrando el archivo secrets.enc.yaml..."
	sops --decrypt secrets.enc.yaml > secrets.yaml
	@echo "Archivo descifrado como secrets.yaml"

# Limpiar archivos generados
clean:
	@echo "Limpiando archivos generados..."
	rm -rf __pycache__
	rm -rf $(VENV)
