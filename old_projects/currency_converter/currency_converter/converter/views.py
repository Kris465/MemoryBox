from django.shortcuts import render
from django.contrib import messages
from .models import Currency
from .utils import update_currency_rates
from decimal import Decimal, InvalidOperation
from loguru import logger


def home(request):
    return render(request, 'home.html')


def contacts(request):
    return render(request, 'contacts.html')


def converter(request):
    currencies = Currency.objects.all()
    result = None
    from_currency = 'USD'
    to_currency = 'RUB'
    amount = Decimal('1')
    currency_date = None

    # Получаем актуальные курсы валют
    try:
        currency_date = update_currency_rates()
    except Exception as e:
        logger.error(f"Ошибка обновления курсов: {e}")
        messages.error(request, 'Не удалось обновить курсы валют. Попробуйте позже.')
        # Используем сохранённые курсы из БД
        if currencies.exists():
            currency_date = currencies.first().date

    if request.method == 'POST':
        try:
            amount_str = request.POST.get('amount', '1')
            amount = Decimal(amount_str)
            if amount <= 0:
                messages.error(request, 'Сумма должна быть больше нуля.')
                amount = Decimal('1')
        except (InvalidOperation, ValueError):
            messages.error(request, 'Некорректная сумма.')
            amount = Decimal('1')

        from_currency = request.POST.get('from_currency', 'USD')
        to_currency = request.POST.get('to_currency', 'RUB')

        try:
            from_curr = Currency.objects.get(char_code=from_currency)
            to_curr = Currency.objects.get(char_code=to_currency)
            result = (amount * from_curr.rate / to_curr.rate).quantize(Decimal('0.0001'))
        except Currency.DoesNotExist:
            messages.error(request, f'Валюта не найдена.')
            logger.error(f"Валюта не найдена: from={from_currency}, to={to_currency}")
        except Exception as e:
            messages.error(request, 'Ошибка при конвертации.')
            logger.error(f"Ошибка конвертации: {e}")

    return render(request, 'converter.html', {
        'currencies': currencies,
        'result': result,
        'amount': amount,
        'from_currency': from_currency,
        'to_currency': to_currency,
        'date': currency_date
    })
