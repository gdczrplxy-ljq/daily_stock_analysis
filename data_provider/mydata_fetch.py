import requests
import time
import json
from cachetools import TTLCache, cached

class MairuiapiDataFetcher:
    def __init__(self, cache_size=100, ttl=300):
        self.cache = TTLCache(maxsize=cache_size, ttl=ttl)

    @cached(cache)
    def fetch_stock_data(self, stock_code):
        api_url = f'https://api.mairuiapi.com/hsstock/latest/?symbol={stock_code}'
        try:
            response = requests.get(api_url)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')  # Log the HTTP error
            return None
        except Exception as err:
            print(f'Other error occurred: {err}')  # Log any other errors
            return None

    def get_real_time_quote(self, stock_code):
        data = self.fetch_stock_data(stock_code)
        if data:
            return data.get('data')  # Adjust based on actual API response structure
        return None

# Example usage:
# fetcher = MairuiapiDataFetcher()
# stock_data = fetcher.get_real_time_quote('AAPL')
# print(stock_data) \n