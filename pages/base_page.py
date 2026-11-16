"""Clase base: acciones comunes que usan todas las paginas (POM)."""
import logging

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

log = logging.getLogger(__name__)


class BasePage:
    def __init__(self, driver, timeout=20):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def abrir(self, url):
        log.info("Abriendo %s", url)
        self.driver.get(url)

    def _visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def _click(self, locator):
        log.info("Click en %s", locator)
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def _escribir(self, locator, texto):
        log.info("Escribiendo en %s", locator)
        campo = self._visible(locator)
        campo.clear()
        campo.send_keys(texto)

    def _texto(self, locator):
        return self._visible(locator).text

    def _existe(self, locator):
        return len(self.driver.find_elements(*locator)) > 0
