"""Paginas de checkout (datos, resumen y confirmacion)."""
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CheckoutPage(BasePage):
    _NOMBRE = (By.ID, "first-name")
    _APELLIDO = (By.ID, "last-name")
    _CODIGO_POSTAL = (By.ID, "postal-code")
    _CONTINUAR = (By.ID, "continue")
    _FINALIZAR = (By.ID, "finish")
    _CONFIRMACION = (By.CSS_SELECTOR, ".complete-header")
    _ERROR = (By.CSS_SELECTOR, "[data-test='error']")

    def completar_datos(self, nombre, apellido, codigo_postal):
        self._escribir(self._NOMBRE, nombre)
        self._escribir(self._APELLIDO, apellido)
        self._escribir(self._CODIGO_POSTAL, codigo_postal)
        return self

    def continuar(self):
        self._click(self._CONTINUAR)
        return self

    def finalizar(self):
        self._click(self._FINALIZAR)
        return self

    def mensaje_confirmacion(self):
        return self._texto(self._CONFIRMACION)

    def obtener_error(self):
        return self._texto(self._ERROR)
