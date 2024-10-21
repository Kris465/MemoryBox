import os
from dotenv import load_dotenv
import requests
from loguru import logger
import pandas as pd


class WbApi:
    def __init__(self, data) -> None:
        load_dotenv()
        self.API_KEY = os.environ['API_KEY']
        self.endpoint = 'https://statistics-api.wildberries.ru/api/v5/supplier/reportDetailByPeriod'
        self.data = data

    def logic(self):

        '''
        Вид получаемых данных из меню:

            self.data = {
            "date_from": date_from,
            "date_to": date_to,
            "report_type": report_type,
            "save_path": save_path
        }
        '''
        match self.data['report_type']:
            case 'Продажи':
                self.endpoint = 'https://statistics-api.wildberries.ru/api/v1/supplier/sales'
            case 'Поставки':
                self.endpoint = 'https://statistics-api.wildberries.ru/api/v1/supplier/incomes'
            case 'Склад':
                self.endpoint = 'https://statistics-api.wildberries.ru/api/v1/supplier/stocks'
            case 'Заказы':
                self.endpoint = 'https://statistics-api.wildberries.ru/api/v1/supplier/orders'
            case 'Отчет о продажах по реализации':
                self.endpoint = 'https://statistics-api.wildberries.ru/api/v5/supplier/reportDetailByPeriod'

        headers = {'Authorization': self.API_KEY,
                   'Content-Type': 'application/json'}
        params = {'dateFrom': self.data['date_from']}
        response = requests.get(self.endpoint, headers=headers, params=params)
        if response.status_code == 200:
            logger.info(f"status_code: {response.status_code}")
            data = response.json()
            df = pd.DataFrame(data)
            df.to_excel('output.xlsx', index=False)
        else:
            logger.error(f"Ошибка: {response.status_code} - {response.text}")
