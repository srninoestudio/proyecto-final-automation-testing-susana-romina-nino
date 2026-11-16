"""Pagina de login de saucedemo.com."""
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):
    URL = "https://www.saucedemo.com/"

    # Locators agrupados al inicio (si cambian, se corrigen aca y nada mas)
    _USUARIO = (By.ID, "user-name")
    _CLAVE = (By.ID, "password")
    _BOTON_LOGIN = (By.ID, "login-button")
    _ERROR = (By.CSS_SELECTOR, "[data-test='error']")

    def abrir_pagina(self):
        self.abrir(self.URL)
        return self

    def completar_usuario(self, usuario):
        if usuario:
            self._escribir(self._USUARIO, usuario)
        return self

    def completar_clave(self, clave):
        if clave:
            self._escribir(self._CLAVE, clave)
        return self

    def click_login(self):
        self._click(self._BOTON_LOGIN)
        return self

    def login(self, usuario, clave):
        return self.completar_usuario(usuario).completar_clave(clave).click_login()

    def obtener_error(self):
        return self._texto(self._ERROR)

    def esta_en_inventario(self):
        return "inventory" in self.driver.current_url
