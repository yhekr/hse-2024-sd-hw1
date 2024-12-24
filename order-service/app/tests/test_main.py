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

def test_assign_order_endpoint():
    data = {"order_id": "order123", "executer_id": "exec123", "locale": "en"}

    response1 = client.post("/assign-order/", json=data)
    assert response1.status_code == 200
    order1 = response1.json()["order"]

    response2 = client.post("/assign-order/", json=data)
    assert response2.status_code == 200
    order2 = response2.json()["order"]

    for key in order1:
        if key != "assign_order_id":
            assert order1[key] == order2[key], f"Mismatch in field '{key}'"

def test_acquire_order_endpoint():
    assign_data = {"order_id": "order123", "executer_id": "exec123", "locale": "en"}
    acquire_data = {"executer_id": "exec123"}

    client.post("/assign-order/", json=assign_data)

    response1 = client.post("/acquire-order/", json=acquire_data)
    assert response1.status_code == 200
    order1 = response1.json()["order"]

    response2 = client.post("/acquire-order/", json=acquire_data)
    assert response2.status_code == 200
    order2 = response2.json()["order"]

    for key in order1:
        assert order1[key] == order2[key], f"Mismatch in field '{key}'"

def test_cancel_order_endpoint():
    assign_data = {"order_id": "order123", "executer_id": "exec123", "locale": "en"}
    cancel_data = {"order_id": "order123"}

    client.post("/assign-order/", json=assign_data)

    response1 = client.post("/cancel-order/", json=cancel_data)
    assert response1.status_code == 200
    order1 = response1.json()["order"]

    response2 = client.post("/cancel-order/", json=cancel_data)
    assert response2.status_code == 200
    order2 = response2.json()["order"]

    for key in order1:
        assert order1[key] == order2[key], f"Mismatch in field '{key}'"
