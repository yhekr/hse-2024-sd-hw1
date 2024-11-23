import requests
from requests.exceptions import RequestException


class RequestHandler:
    @staticmethod
    def fetch_data(url: str, params: dict = None) -> dict:
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            data = response.json()
            return data
        except RequestException as e:
            print(f"Network error while fetching data from {url}: {e}")
            raise
        except ValueError as e:
            print(f"Error parsing JSON data from {url}: {e}")
            raise
        except KeyError as e:
            print(f"Missing expected data field in response from {url}: {e}")
            raise
