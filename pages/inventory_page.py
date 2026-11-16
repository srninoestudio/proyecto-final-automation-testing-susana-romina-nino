"""Pagina de productos (despues de loguearse)."""
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

from pages.base_page import BasePage


class InventoryPage(BasePage):
    _TITULO = (By.CSS_SELECTOR, ".title")
    _BADGE_CARRITO = (By.CSS_SELECTOR, ".shopping_cart_badge")
    _ICONO_CARRITO = (By.CSS_SELECTOR, "[data-test='shopping-cart-link']")
    _NOMBRES = (By.CSS_SELECTOR, ".inventory_item_name")
    _ORDENAR = (By.CSS_SELECTOR, "[data-test='product-sort-container']")
    _MENU = (By.ID, "react-burger-menu-btn")
    _LOGOUT = (By.ID, "logout_sidebar_link")

    def obtener_titulo(self):
        return self._texto(self._TITULO)

    def agregar_producto(self, slug):
        """slug: nombre del producto con guiones, ej. 'sauce-labs-backpack'."""
        self._click((By.ID, f"add-to-cart-{slug}"))
        return self

    def quitar_producto(self, slug):
        self._click((By.ID, f"remove-{slug}"))
        return self

    def cantidad_en_carrito(self):
        if not self._existe(self._BADGE_CARRITO):
            return 0
        return int(self._texto(self._BADGE_CARRITO))

    def ir_al_carrito(self):
        self._click(self._ICONO_CARRITO)
        self.wait.until(EC.url_contains("cart"))
        return self

    def ordenar_por(self, valor):
        """valor: 'az', 'za', 'lohi' o 'hilo'."""
        Select(self._visible(self._ORDENAR)).select_by_value(valor)
        return self

    def nombres_productos(self):
        self._visible(self._NOMBRES)
        return [e.text for e in self.driver.find_elements(*self._NOMBRES)]

    def cerrar_sesion(self):
        self._click(self._MENU)
        self._click(self._LOGOUT)
        self._visible((By.ID, "login-button"))
        return self