from django.shortcuts import render
from .models import Currency
from .utils import update_currency_rates
from decimal import Decimal


def home(request):
    return render(request, 'home.html')


def contacts(request):
    return render(request, 'contacts.html')


def converter(request):
    date = update_currency_rates()
    currencies = Currency.objects.all()

    result = None
    from_currency = 'USD'
    to_currency = 'RUB'
    amount = 1

    if request.method == 'POST':
        amount = Decimal(request.POST.get('amount', 1))
        from_currency = request.POST.get('from_currency', 'USD')
        to_currency = request.POST.get('to_currency', 'RUB')

        from_curr = Currency.objects.get(char_code=from_currency)
        to_curr = Currency.objects.get(char_code=to_currency)

        result = (amount * from_curr.rate / to_curr.rate).quantize(Decimal('0.0001'))

    return render(request, 'converter.html', {
        'currencies': currencies,
        'result': result,
        'amount': amount,
        'from_currency': from_currency,
        'to_currency': to_currency,
        'date': date
    })
