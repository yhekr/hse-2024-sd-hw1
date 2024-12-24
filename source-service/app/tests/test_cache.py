from unittest.mock import patch, MagicMock
from services.cache import get_cache, set_cache, CACHE_KEY


@patch("services.cache.redis_client")
def test_get_cache_success(mock_redis_client):
    mock_redis_client.get.return_value = b'{"coin_coeff_settings": {"key": "value"}}'

    cached_data = get_cache()
    assert cached_data == b'{"coin_coeff_settings": {"key": "value"}}'
    mock_redis_client.get.assert_called_once_with(CACHE_KEY)


@patch("services.cache.redis_client")
def test_set_cache_success(mock_redis_client):
    mock_redis_client.set.return_value = True
    set_cache({"key": "value"})
    mock_redis_client.set.assert_called_once_with(CACHE_KEY, '{"key": "value"}', ex=60)

@patch("services.cache.redis_client")
def test_cache_liveness(mock_redis_client):
    mock_redis_client.set.return_value = True
    config_data = {"setting": "initial_value"}
    set_cache(config_data)
    mock_redis_client.set.assert_called_once_with(CACHE_KEY, '{"setting": "initial_value"}', ex=60)

    mock_redis_client.get.return_value = b'{"setting": "initial_value"}'
    cached_data = get_cache()
    assert cached_data == b'{"setting": "initial_value"}'
    mock_redis_client.get.assert_called_once_with(CACHE_KEY)

    mock_redis_client.set.reset_mock()
    updated_config_data = {"setting": "updated_value"}
    set_cache(updated_config_data)
    mock_redis_client.set.assert_called_once_with(CACHE_KEY, '{"setting": "updated_value"}', ex=60)

    mock_redis_client.get.return_value = b'{"setting": "updated_value"}'
    updated_cached_data = get_cache()
    assert updated_cached_data == b'{"setting": "updated_value"}'
    mock_redis_client.get.assert_called_with(CACHE_KEY)

