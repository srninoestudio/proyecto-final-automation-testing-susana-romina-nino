"""Pagina del carrito."""
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CartPage(BasePage):
    _ITEMS = (By.CSS_SELECTOR, ".inventory_item_name")
    _BOTON_CHECKOUT = (By.ID, "checkout")

    def nombres_en_carrito(self):
        return [e.text for e in self.driver.find_elements(*self._ITEMS)]

    def click_checkout(self):
        self._click(self._BOTON_CHECKOUT)
        return self
