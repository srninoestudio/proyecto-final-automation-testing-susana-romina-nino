"""Pruebas de productos y carrito."""
import pytest

from pages.cart_page import CartPage


@pytest.mark.ui
def test_agregar_producto_al_carrito(pagina_inventario):
    pagina_inventario.agregar_producto("sauce-labs-backpack")
    assert pagina_inventario.cantidad_en_carrito() == 1
    pagina_inventario.ir_al_carrito()
    carrito = CartPage(pagina_inventario.driver)
    assert "Sauce Labs Backpack" in carrito.nombres_en_carrito()


@pytest.mark.ui
def test_quitar_producto_del_carrito(pagina_inventario):
    pagina_inventario.agregar_producto("sauce-labs-backpack")
    pagina_inventario.quitar_producto("sauce-labs-backpack")
    assert pagina_inventario.cantidad_en_carrito() == 0


@pytest.mark.ui
def test_ordenar_productos_de_la_z_a_la_a(pagina_inventario):
    pagina_inventario.ordenar_por("za")
    nombres = pagina_inventario.nombres_productos()
    assert nombres == sorted(nombres, reverse=True)


@pytest.mark.ui
def test_cerrar_sesion(pagina_inventario):
    pagina_inventario.cerrar_sesion()
    assert "saucedemo.com" in pagina_inventario.driver.current_url
    assert "inventory" not in pagina_inventario.driver.current_url
