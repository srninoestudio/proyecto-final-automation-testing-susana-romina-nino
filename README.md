Autora: Susana Romina Niño
# Proyecto final: framework de automatización de pruebas

## Propósito
Framework de testing automatizado en Python que prueba la UI de https://www.saucedemo.com
(Selenium WebDriver) y la API pública https://jsonplaceholder.typicode.com (Requests).

## Tecnologías
Python, Pytest, Selenium WebDriver, Requests, pytest-html, Git y GitHub.

## Estructura
```
pages/        Page Objects (una clase por página, con locators y acciones)
tests/ui/     Pruebas de interfaz: login, inventario, checkout
tests/api/    Pruebas de API: GET, POST, DELETE y un flujo encadenado
utils/        Lectura de datos desde CSV y JSON
data/         Datos de prueba (login.csv, checkout.json)
conftest.py   Fixtures y captura de pantalla automática al fallar
pytest.ini    Reporte HTML, logging y markers
```

## Instalación
```
python -m venv .venv
.venv\Scripts\activate        # en Windows (en Mac/Linux: source .venv/bin/activate)
pip install -r requirements.txt
```
Requiere Google Chrome instalado (Selenium descarga el driver solo).

## Cómo ejecutar
```
pytest                      # todas las pruebas
pytest -m ui                # solo UI
pytest -m api               # solo API
pytest -m e2e               # solo flujos completos
```
Para correr sin abrir la ventana del navegador: `set HEADLESS=1` (Windows) o `HEADLESS=1 pytest` (Mac/Linux).

## Reportes
- `reports/reporte.html`: tests ejecutados, estado, duración y capturas de los fallos.
- `screenshots/`: capturas con fecha, hora y nombre del test.
- `logs/suite.log`: registro de los pasos clave para depurar.
