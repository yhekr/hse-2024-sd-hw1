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
