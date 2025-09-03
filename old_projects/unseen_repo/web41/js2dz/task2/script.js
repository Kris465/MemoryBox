document.getElementById('symbolButton').addEventListener('click', function() {
    const number = Number(document.getElementById('symbolInput').value);
    const symbolResult = document.getElementById('symbolResult');
    
    switch (number) {
        case 0:
            symbolResult.textContent = ')';
            break;
        case 1:
            symbolResult.textContent = '!';
            break;
        case 2:
            symbolResult.textContent = '@';
            break;
        case 3:
            symbolResult.textContent = '#';
            break;
        case 4:
            symbolResult.textContent = '$';
            break;
        case 5:
            symbolResult.textContent = '%';
            break;
        case 6:
            symbolResult.textContent = '^';
            break;
        case 7:
            symbolResult.textContent = '&';
            break;
        case 8:
            symbolResult.textContent = '*';
            break;
        case 9:
            symbolResult.textContent = '(';
            break;
        default:
            symbolResult.textContent = 'Некорректный ввод.';
            break;
    }
});