import pytest
from unittest.mock import patch, MagicMock
from services.data_requests import (
    get_order_data,
    get_zone_info,
    get_executer_profile,
    get_configs,
    get_toll_roads
)
from models.model import OrderData, ZoneData, ExecuterProfile, ConfigMap, TollRoadsData


@patch("services.data_requests.RequestHandler.fetch_data")
def test_get_order_data(mock_fetch_data):
    mock_fetch_data.return_value = {
        "zone_id": "zone123",
        "user_id": "user123",
        "base_coin_amount": 100.0
    }

    result = get_order_data("order123")
    assert isinstance(result, OrderData)
    assert result.id == "order123"
    assert result.zone_id == "zone123"
    assert result.user_id == "user123"
    assert result.base_coin_amount == 100.0
    mock_fetch_data.assert_called_once_with("http://mock-sources-server:3629/order-data", params={"id": "order123"})


@patch("services.data_requests.RequestHandler.fetch_data")
def test_get_zone_info(mock_fetch_data):
    mock_fetch_data.return_value = {
        "coin_coeff": 1.5,
        "display_name": "Test Zone"
    }

    result = get_zone_info("zone123")
    assert isinstance(result, ZoneData)
    assert result.id == "zone123"
    assert result.coin_coeff == 1.5
    assert result.display_name == "Test Zone"
    mock_fetch_data.assert_called_once_with("http://mock-sources-server:3629/zone-data", params={"id": "zone123"})


@patch("services.data_requests.RequestHandler.fetch_data")
def test_get_executer_profile(mock_fetch_data):
    mock_fetch_data.return_value = {
        "tags": ["fast", "reliable"],
        "rating": 4.8
    }

    result = get_executer_profile("exec123")
    assert isinstance(result, ExecuterProfile)
    assert result.id == "exec123"
    assert result.tags == ["fast", "reliable"]
    assert result.rating == 4.8
    mock_fetch_data.assert_called_once_with("http://mock-sources-server:3629/executer-profile", params={"id": "exec123"})


@patch("services.data_requests.get_cache")
@patch("services.data_requests.set_cache")
@patch("services.data_requests.RequestHandler.fetch_data")
def test_get_configs_with_and_without_cache(mock_fetch_data, mock_set_cache, mock_get_cache):
    # Test with cache hit
    mock_get_cache.return_value = '{"coin_coeff_settings": {"key": "value"}}'

    result = get_configs()
    assert isinstance(result, ConfigMap)
    assert result.coin_coeff_settings == {"key": "value"}
    mock_fetch_data.assert_not_called()
    mock_set_cache.assert_not_called()

    # Test with cache miss
    mock_get_cache.return_value = None
    mock_fetch_data.return_value = {"coin_coeff_settings": {"key": "value"}}

    result = get_configs()
    assert isinstance(result, ConfigMap)
    assert result.coin_coeff_settings == {"key": "value"}
    mock_set_cache.assert_called_once_with({"coin_coeff_settings": {"key": "value"}})


@patch("services.data_requests.RequestHandler.fetch_data")
def test_get_toll_roads(mock_fetch_data):
    mock_fetch_data.return_value = {
        "bonus_amount": 50.0
    }

    result = get_toll_roads("Test Zone")
    assert isinstance(result, TollRoadsData)
    assert result.bonus_amount == 50.0
    mock_fetch_data.assert_called_once_with("http://mock-sources-server:3629/toll-roads", params={"zone_display_name": "Test Zone"})
