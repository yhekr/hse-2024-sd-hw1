import pytest
from unittest.mock import patch, MagicMock
from services.request_handler import RequestHandler


@patch("services.request_handler.requests.get")
def test_fetch_data_success(mock_get):
    mock_response = MagicMock()
    mock_response.json.return_value = {"key": "value"}
    mock_response.status_code = 200
    mock_get.return_value = mock_response

    result = RequestHandler.fetch_data("http://example.com")
    assert result == {"key": "value"}
    mock_get.assert_called_once_with("http://example.com", params=None)


@patch("services.request_handler.requests.get")
def test_fetch_data_network_error(mock_get):
    mock_get.side_effect = Exception("Network error")

    with pytest.raises(Exception, match="Network error"):
        RequestHandler.fetch_data("http://example.com")
