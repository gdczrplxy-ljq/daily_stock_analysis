import requests
import time
import json
from cachetools import TTLCache, cached

class MairuiapiDataFetcher:
    def __init__(self, cache_size=100, ttl=300, api_key='670F47A4-C18B-47CC-A4E1-9C5178B69603'):
        self.cache = TTLCache(maxsize=cache_size, ttl=ttl)
        self.api_key = api_key
        self.base_url = 'https://api.mairuiapi.com/hsstock/latest'

    @cached(cache={})
    def fetch_stock_data(self, stock_code):
        # 构建API URL: https://api.mairuiapi.com/hsstock/latest/{stock_code}/d/n/{api_key}
        api_url = f'{self.base_url}/{stock_code}/d/n/{self.api_key}'
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
# stock_data = fetcher.get_real_time_quote('000001.SZ')
# print(stock_data)