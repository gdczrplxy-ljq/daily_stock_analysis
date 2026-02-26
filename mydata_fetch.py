import requests
import logging
import random
import time
from base_fetcher import BaseFetcher

# Configure logging
logging.basicConfig(level=logging.INFO)

class MairuiapiDataFetcher(BaseFetcher):
    API_URL = 'https://api.mairuiapi.com/hsstock/latest/'
    API_KEY = '670F47A4-C18B-47CC-A4E1-9C5178B69603'

    def __init__(self):
        super().__init__()

    def fetch_data(self, stock_code):
        try:
            response = requests.get(self.API_URL, params={'stock_code': stock_code}, headers={'Authorization': self.API_KEY})
            response.raise_for_status()
            return self.normalize_data(response.json())
        except requests.exceptions.RequestException as e:
            logging.error(f'Error fetching data for {stock_code}: {e}')
            return None

    def fetch_historical_data(self, stock_code):
        # Fetch historical data logic here
        pass

    def fetch_realtime_quotes(self, stock_code):
        logging.info(f'Fetching real-time quote for: {stock_code}')
        return self.fetch_data(stock_code)

    def normalize_data(self, data):
        # Example normalization logic
        normalized_data = {  
            'symbol': data.get('symbol'),
            'price': data.get('current_price'),
            'timestamp': data.get('timestamp'),
        }
        return normalized_data

    def validate_stock_code(self, stock_code):
        # Stock code validation logic
        return True

    def rate_limit(self):
        sleep_time = random.uniform(1, 3)  # Random sleep to limit rate
        logging.info(f'Rate limiting for {sleep_time:.2f} seconds')
        time.sleep(sleep_time)

if __name__ == '__main__':
    fetcher = MairuiapiDataFetcher()
    stock_code = input('Enter stock code: ')
    if fetcher.validate_stock_code(stock_code):
        fetcher.rate_limit()
        quote = fetcher.fetch_realtime_quotes(stock_code)
        logging.info(f'Real-time quote: {quote}')
    else:
        logging.error('Invalid stock code!')
