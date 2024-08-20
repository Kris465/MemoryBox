import os
import requests
import json
from dotenv import load_dotenv


load_dotenv()
API_KEY = os.environ['API_KEY']
BASE_URL = 'https://statistics-api.wildberries.ru'


headers = {
    'Authorization': API_KEY,    'Content-Type': 'application/json'
}


def get_sales_statistics(start_date):
    endpoint = f"{BASE_URL}/api/v1/supplier/sales"
    params = {'dateFrom': start_date}
    response = requests.get(endpoint, headers=headers, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Ошибка: {response.status_code} - {response.text}")
        return None


# Пример использования функцииstart_date = '2024-08-19'
sales_data = get_sales_statistics(start_date)
if sales_data:
    res = json.dumps(sales_data, ensure_ascii=False)
    file = open('output.json', 'w')
    file.write(res)
    file.close()
