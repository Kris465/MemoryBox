document.getElementById('curensyButton').addEventListener('click', function() {
    const colichestvo = Number(document.getElementById('curensyInput').value);
    const curensyResult = document.getElementById('curensyResult');
    const curensy = prompt('Введите валюту для конвертации: ');
    let convertedColichestvo;
    
    switch (curensy) {
        case 'EUR':
            convertedColichestvo = colichestvo * 0.9;
            break;
        case 'UAN':
            convertedColichestvo = colichestvo * 7.28;
            break;
        case 'AZN':
            convertedColichestvo = colichestvo * 0.59;
            break;
        default:
            curensyResult.textContent = 'Неверная валюта';
            return;
    }
    curensyResult.textContent = `Сумма в ${curensy}: ${convertedColichestvo.toFixed(2)}`;
    
});