document.getElementById('currencyButton').addEventListener('click', function() {
    const amount = Number(document.getElementById('currencyInput').value);
    const currencyResult = document.getElementById('currencyResult');
    const currency = prompt("Введите валюту для конвертации (EUR, UAN, AZN):").toUpperCase();
    let convertedAmount;

    switch (currency) {
        case 'EUR':
            convertedAmount = amount * 0.9;
            break;
        case 'UAN':
            convertedAmount = amount * 7.28;
            break;
        case 'AZN':
            convertedAmount = amount * 0.59;
            break;
        default:
            currencyResult.textContent = 'Неверная валюта.';
            return;
    }

    currencyResult.textContent = `Сумма в ${currency}: ${convertedAmount.toFixed(2)}`;
});
