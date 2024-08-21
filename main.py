def main():
    print("Hello")
    date = input("Введите дату (YYYY-MM-DD): ")
    wb_api = WbApi(date)
    wb_api.get_statistics()


if __name__ == '__main__':
    main()




import os
import requests
import json
from dotenv import load_dotenv
from loguru import logger


load_dotenv()
API_KEY = os.environ['API_KEY']
BASE_URL = 'https://statistics-api.wildberries.ru'


logger.add("file.log",
           format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}",
           rotation='3 days', backtrace=True, diagnose=True)

headers = {
    'Authorization': API_KEY,    'Content-Type': 'application/json'
}


def get_sales_statistics(start_date):
    endpoint = f"{BASE_URL}/api/v1/supplier/sales"
    params = {'dateFrom': start_date}
    response = requests.get(endpoint, headers=headers, params=params)
    if response.status_code == 200:
        logger.info(f"status_code: {response.status_code}")
        return response.json()
    else:
        logger.error(f"Ошибка: {response.status_code} - {response.text}")
        return None


''' Формат даты = "2024-08-19" '''

start_date = '2024-08-20'
sales_data = get_sales_statistics(start_date)
if sales_data:
    res = json.dumps(sales_data, ensure_ascii=False)
    file = open('output.json', 'w')
    file.write(res)
    file.close()
