"""Flujo completo de compra (end-to-end) y un caso negativo, con datos desde JSON."""
import pytest

from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from utils.datos import leer_json

DATOS = leer_json("checkout.json")


@pytest.mark.ui
@pytest.mark.e2e
def test_compra_completa(pagina_inventario):
    for producto in DATOS["productos"]:
        pagina_inventario.agregar_producto(producto)
    assert pagina_inventario.cantidad_en_carrito() == len(DATOS["productos"])

    pagina_inventario.ir_al_carrito()
    CartPage(pagina_inventario.driver).click_checkout()

    comprador = DATOS["comprador"]
    checkout = CheckoutPage(pagina_inventario.driver)
    checkout.completar_datos(
        comprador["nombre"], comprador["apellido"], comprador["codigo_postal"]
    ).continuar().finalizar()
    assert "Thank you for your order" in checkout.mensaje_confirmacion()


@pytest.mark.ui
def test_checkout_sin_datos_muestra_error(pagina_inventario):
    pagina_inventario.agregar_producto("sauce-labs-backpack").ir_al_carrito()
    CartPage(pagina_inventario.driver).click_checkout()
    checkout = CheckoutPage(pagina_inventario.driver).continuar()
    assert "First Name is required" in checkout.obtener_error()
