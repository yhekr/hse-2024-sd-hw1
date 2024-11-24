import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_assign_order_endpoint():
    response = client.post(
        "/assign-order/",
        json={"order_id": "order123", "executer_id": "exec123", "locale": "en"}
    )
    assert response.status_code == 200
    assert response.json()["message"] == "Order assigned successfully"


def test_acquire_order_endpoint():
    client.post("/assign-order/", json={"order_id": "order123", "executer_id": "exec123", "locale": "en"})

    response = client.post("/acquire-order/", json={"executer_id": "exec123"})
    assert response.status_code == 200
    assert response.json()["message"] == "Order acquired successfully"


def test_cancel_order_endpoint():
    client.post("/assign-order/", json={"order_id": "order123", "executer_id": "exec123", "locale": "en"})

    response = client.post("/cancel-order/", json={"order_id": "order123"})
    assert response.status_code == 200
    assert response.json()["message"] == "Order cancelled successfully"
