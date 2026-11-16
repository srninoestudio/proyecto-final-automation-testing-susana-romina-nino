"""Pruebas de API con Requests sobre JSONPlaceholder."""
import logging

import pytest
import requests

log = logging.getLogger(__name__)
BASE_URL = "https://jsonplaceholder.typicode.com"
TIMEOUT = 10


@pytest.mark.api
def test_get_post_existente():
    r = requests.get(f"{BASE_URL}/posts/1", timeout=TIMEOUT)
    log.info("GET /posts/1 -> %s", r.status_code)
    assert r.status_code == 200
    cuerpo = r.json()
    assert {"userId", "id", "title", "body"} <= cuerpo.keys()
    assert isinstance(cuerpo["id"], int) and cuerpo["id"] == 1
    assert r.elapsed.total_seconds() < 5


@pytest.mark.api
def test_get_post_inexistente_devuelve_404():
    r = requests.get(f"{BASE_URL}/posts/99999", timeout=TIMEOUT)
    assert r.status_code == 404


@pytest.mark.api
def test_post_crea_recurso():
    datos = {"title": "Prueba QA", "body": "Contenido de prueba", "userId": 1}
    r = requests.post(f"{BASE_URL}/posts", json=datos, timeout=TIMEOUT)
    log.info("POST /posts -> %s", r.status_code)
    assert r.status_code == 201
    cuerpo = r.json()
    assert cuerpo["title"] == datos["title"]
    assert isinstance(cuerpo["id"], int)


@pytest.mark.api
def test_delete_post():
    r = requests.delete(f"{BASE_URL}/posts/1", timeout=TIMEOUT)
    assert r.status_code == 200
    assert r.json() == {}


@pytest.mark.api
@pytest.mark.e2e
def test_encadenado_usuario_y_sus_posts():
    """Una peticion depende de la otra: primero el usuario, despues sus posts."""
    usuario = requests.get(f"{BASE_URL}/users/1", timeout=TIMEOUT).json()
    r = requests.get(f"{BASE_URL}/posts", params={"userId": usuario["id"]}, timeout=TIMEOUT)
    assert r.status_code == 200
    posts = r.json()
    assert len(posts) > 0
    assert all(p["userId"] == usuario["id"] for p in posts)
