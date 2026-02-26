import requests

class MyDataFetcher(BaseFetcher):
    def __init__(self):
        super().__init__()

    def fetch_stock_data(self, stock_code):
        url = f'https://api.mairuiapi.com/hsstock/latest/?code={{stock_code}}'
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return {'error': 'Failed to fetch data', 'status_code': response.status_code}