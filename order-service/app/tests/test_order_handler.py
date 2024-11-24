from unittest.mock import patch, MagicMock
import pytest
from datetime import datetime
from services.order_handler import (
    handle_assign_order_request,
    handle_acquire_order_request,
    handle_cancel_order_request
)
from models.model import AssignedOrder
from db.database import save_order_to_db
import uuid


@patch("services.order_handler.stub.GetOrderInfo")
def test_handle_assign_order_request(mock_get_order_info):
    mock_get_order_info.return_value = MagicMock(
        order_price=MagicMock(
            base_order_price=100.0,
            coin_coef=1.5,
            coin_bonus_amount=20.0,
            final_order_price=170.0
        ),
        executor_profile=MagicMock(rating=9),
        zone_display_name="Test Zone"
    )

    order = handle_assign_order_request("order123", "exec123", "en")
    assert order is not None
    assert order.order_id == "order123"
    assert order.final_coin_amount == 170.0
    assert "Order at zone" in order.route_information


def test_handle_acquire_order_request():
    order = AssignedOrder(
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

    save_order_to_db(order)

    acquired_order = handle_acquire_order_request("exec123")
    assert acquired_order is not None
    assert acquired_order.order_id == "order123"
    assert acquired_order.acquire_time is not None


def test_handle_cancel_order_request():
    order = AssignedOrder(
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

    save_order_to_db(order)

    cancelled_order = handle_cancel_order_request("order123")
    assert cancelled_order is not None
    assert cancelled_order.is_canceled is True
