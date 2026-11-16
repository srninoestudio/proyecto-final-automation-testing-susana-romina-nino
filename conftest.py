"""Fixtures y hooks compartidos por todas las pruebas."""
import base64
import logging
import os
import re
from datetime import datetime
from pathlib import Path

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage

RAIZ = Path(__file__).resolve().parent
CARPETA_CAPTURAS = RAIZ / "screenshots"
log = logging.getLogger(__name__)


def pytest_configure(config):
    """Crea las carpetas de salida antes de correr los tests."""
    for carpeta in ("logs", "reports", "screenshots"):
        (RAIZ / carpeta).mkdir(exist_ok=True)


@pytest.fixture
def driver():
    """Abre Chrome para cada test y lo cierra al terminar (tests independientes)."""
    opciones = Options()
    if os.getenv("HEADLESS", "0") == "1":
        opciones.add_argument("--headless=new")
    opciones.add_argument("--window-size=1366,768")
    # Evita el aviso de "cambiar contrasena" de Chrome
    opciones.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
    })
    opciones.add_experimental_option("excludeSwitches", ["enable-automation"])
    log.info("Abriendo navegador")
    navegador = webdriver.Chrome(options=opciones)
    yield navegador
    log.info("Cerrando navegador")
    navegador.quit()


@pytest.fixture
def pagina_inventario(driver):
    """Deja al test ya logueado y en la pagina de productos."""
    LoginPage(driver).abrir_pagina().login("standard_user", "secret_sauce")
    return InventoryPage(driver)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Si un test de UI falla: guarda captura con fecha/hora y nombre, y la inserta en el reporte HTML."""
    salida = yield
    reporte = salida.get_result()
    if reporte.when != "call" or not reporte.failed:
        return
    navegador = item.funcargs.get("driver")
    if navegador is None:
        return
    marca = datetime.now().strftime("%Y%m%d_%H%M%S")
    nombre_seguro = re.sub(r"[^A-Za-z0-9_-]+", "_", item.name)
    ruta = CARPETA_CAPTURAS / f"{marca}_{nombre_seguro}.png"
    navegador.save_screenshot(str(ruta))
    log.error("Test fallido: %s. Captura guardada en %s", item.name, ruta)
    try:
        from pytest_html import extras
        imagen = base64.b64encode(ruta.read_bytes()).decode()
        reporte.extras = getattr(reporte, "extras", []) + [extras.png(imagen)]
    except ImportError:
        pass
