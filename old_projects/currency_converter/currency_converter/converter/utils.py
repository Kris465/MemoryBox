import requests
from datetime import datetime, date
from decimal import Decimal
from .models import Currency
from loguru import logger


def update_currency_rates():
    """Обновляет курсы валют из API ЦБ РФ.
    
    Returns:
        date: Дата курсов валют.
        
    Raises:
        Exception: При ошибке получения или обработки данных API.
    """
    url = 'https://www.cbr-xml-daily.ru/daily_json.js'
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
    except requests.RequestException as e:
        logger.error(f"Ошибка при получении данных API: {e}")
        raise Exception(f"Не удалось получить курсы валют: {e}")
    except ValueError as e:
        logger.error(f"Ошибка при разборе JSON: {e}")
        raise Exception(f"Некорректный формат данных API: {e}")

    try:
        date_str = data['Date']
        currency_date = datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%S%z').date()
    except (KeyError, ValueError) as e:
        logger.error(f"Ошибка при обработке даты: {e}")
        raise Exception(f"Некорректный формат даты в API: {e}")

    try:
        Currency.objects.update_or_create(
            char_code='RUB',
            defaults={
                'name': 'Российский рубль',
                'rate': Decimal('1'),
                'date': currency_date
            }
        )

        for char_code, currency_data in data['Valute'].items():
            Currency.objects.update_or_create(
                char_code=char_code,
                defaults={
                    'name': currency_data['Name'],
                    'rate': Decimal(str(currency_data['Value'])),
                    'date': currency_date
                }
            )
    except Exception as e:
        logger.error(f"Ошибка при сохранении валют в БД: {e}")
        raise Exception(f"Не удалось сохранить курсы валют: {e}")

    return currency_date
