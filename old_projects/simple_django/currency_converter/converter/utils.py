import requests
from datetime import datetime
from decimal import Decimal
from .models import Currency


def update_currency_rates():
    url = 'https://www.cbr-xml-daily.ru/daily_json.js'
    response = requests.get(url)
    data = response.json()

    date = datetime.strptime(data['Date'], '%Y-%m-%dT%H:%M:%S%z').date()

    Currency.objects.update_or_create(
        char_code='RUB',
        defaults={
            'name': 'Российский рубль',
            'rate': Decimal('1'),
            'date': date
        }
    )

    for char_code, currency_data in data['Valute'].items():
        Currency.objects.update_or_create(
            char_code=char_code,
            defaults={
                'name': currency_data['Name'],
                'rate': Decimal(str(currency_data['Value'])),
                'date': date
            }
        )

    return date
