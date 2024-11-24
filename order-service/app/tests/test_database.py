import pytest
from unittest.mock import MagicMock
from datetime import datetime
from models.model import AssignedOrder
from db.database import (
    init_db, save_order_to_db, get_order_from_db, delete_order_from_db, update_order_acquire_time, cancel_order, get_latest_order_id_for_executer
)
from db.database import drop_db
import uuid

@pytest.fixture(scope="module")
def sample_order():
    return AssignedOrder(
        assign_order_id=str(uuid.uuid4()),
        order_id="order123",
        executer_id="exec123",
        base_coin_amount=100.0,
        coin_coef=1.5,
        bonus_amount=20.0,
        final_coin_amount=170.0,
        route_information="Test Route",
        assign_time=datetime.now(),
        acquire_time=None,
        is_canceled=False
    )


@pytest.fixture(autouse=True)
def setup_database():
    drop_db()
    init_db()  # Создание тестовой базы данных
    yield
    # После выполнения тестов, очищаем данные
    drop_db()


def test_save_and_get_order(sample_order):
    save_order_to_db(sample_order)
    retrieved_order = get_order_from_db(sample_order.order_id)

    assert retrieved_order is not None
    assert retrieved_order.order_id == sample_order.order_id
    assert retrieved_order.executer_id == sample_order.executer_id


def test_update_acquire_time(sample_order):
    save_order_to_db(sample_order)
    acquire_time = datetime.now()
    update_order_acquire_time(sample_order.order_id, acquire_time)

    updated_order = get_order_from_db(sample_order.order_id)
    assert updated_order.acquire_time == acquire_time


def test_cancel_order(sample_order):
    save_order_to_db(sample_order)
    cancel_order(sample_order.order_id)

    cancelled_order = get_order_from_db(sample_order.order_id)
    assert cancelled_order.is_canceled is True


def test_delete_order(sample_order):
    save_order_to_db(sample_order)
    delete_order_from_db(sample_order.order_id)

    deleted_order = get_order_from_db(sample_order.order_id)
    assert deleted_order is None


def test_get_latest_order(sample_order):
    save_order_to_db(sample_order)
    latest_order_id = get_latest_order_id_for_executer(sample_order.executer_id)

    assert latest_order_id == sample_order.order_id
