"""Lectura de datos de prueba desde archivos externos (CSV y JSON)."""
import csv
import json
from pathlib import Path

CARPETA_DATOS = Path(__file__).resolve().parent.parent / "data"


def leer_csv_login():
    """Convierte data/login.csv en una lista de tuplas:
    (usuario, clave, debe_funcionar, descripcion)."""
    casos = []
    with open(CARPETA_DATOS / "login.csv", newline="", encoding="utf-8") as archivo:
        for fila in csv.DictReader(archivo):
            casos.append((
                fila["usuario"],
                fila["clave"],
                fila["debe_funcionar"].strip().lower() == "true",
                fila["descripcion"],
            ))
    return casos


def leer_json(nombre_archivo):
    """Lee un archivo JSON de la carpeta data/ y devuelve su contenido."""
    with open(CARPETA_DATOS / nombre_archivo, encoding="utf-8") as archivo:
        return json.load(archivo)
