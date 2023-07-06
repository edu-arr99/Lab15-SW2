import pytest
from app import app

def test_hello():
    response = app.test_client().get("/hello")
    assert response.status_code == 200
    assert response.data.decode('utf-8') == '"hello"\n'

def test_suma():
    response = app.test_client().get("/suma/4/5")
    assert response.status_code == 200
    assert response.data.decode('utf-8') == '9\n'