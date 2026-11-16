"""Pruebas de login (parametrizadas con data/login.csv). Incluye casos negativos."""
import logging

import pytest

from pages.login_page import LoginPage
from utils.datos import leer_csv_login

log = logging.getLogger(__name__)
CASOS = leer_csv_login()


@pytest.mark.ui
@pytest.mark.parametrize(
    "usuario, clave, debe_funcionar, descripcion",
    CASOS,
    ids=[c[3] for c in CASOS],
)
def test_login(driver, usuario, clave, debe_funcionar, descripcion):
    log.info("Caso de login: %s", descripcion)
    pagina = LoginPage(driver).abrir_pagina().login(usuario, clave)
    if debe_funcionar:
        assert pagina.esta_en_inventario()
    else:
        assert not pagina.esta_en_inventario()
        assert "Epic sadface" in pagina.obtener_error()
