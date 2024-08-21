import os
from dotenv import load_dotenv
import requests
from loguru import logger


class WbApi:
    def __init__(self, date) -> None:
        load_dotenv()
        self.API_KEY = os.environ['API_KEY']
        self.BASE_URL = 'https://statistics-api.wildberries.ru'
        self.date = date

    def get_sales_statistics(self):
        print(self.API_KEY)
        headers = {'Authorization': self.API_KEY,
                   'Content-Type': 'application/json'}
        endpoint = f"{self.BASE_URL}/api/v1/supplier/sales"
        params = {'dateFrom': self.date}
        response = requests.get(endpoint, headers=headers, params=params)
        if response.status_code == 200:
            logger.info(f"status_code: {response.status_code}")
            return response.json()
        else:
            logger.error(f"Ошибка: {response.status_code} - {response.text}")
            return None
