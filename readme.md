# Testing


## Instrucciones de ejecución
1. Ejecutar el comando `make run-app`
2. Abrimos otra terminal para realizar las pruebas de testing.
3. Ejecutar el comando `make test`
4. Ejecutar el comando `make pylint`
5. Ejecutar el comando `make coverage` para la cobertura
6. Ejecutar el comando `make trivy` para el analisis de seguridad
7. Ejecutar el comando `make clean` para limpiar el entorno de trabajo.

## Reporte de seguridad de Trivy
El reporte de seguridad nos muestra un fallo de intregridad para la versión de python `3.12.4` en Ubuntu. 
![Reporte de seguridad de trivy](image.png)
[Link al reporte de trivy](https://avd.aquasec.com/nvd/cve-2022-42969)

## Reporte de cobertura
Nos muestra que la calidad del codigo de media en todo el proyecto es del 94% de cobertura.
![Reporte de cobertura](image-1.png)

## Referencias
- https://earthly.dev/blog/python-makefile/
- https://stackoverflow.com/questions/40720369/how-to-use-wait-in-makefile-when-i-use-it-through-nmake-in-windows
- [Ver prompts](prompt.md)