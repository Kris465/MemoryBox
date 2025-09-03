document.getElementById('submitButton').addEventListener('click', function() {
    const input = document.getElementById('numberInput').value;
    const result = document.getElementById('result');
    
    // Преобразуем ввод в число
    const number = Number(input);
    
    // Определяем название цифры
    switch (number) {
        case 0:
            result.textContent = 'ноль';
            break;
        case 1:
            result.textContent = 'единица';
            break;
        case 2:
            result.textContent = 'двойка';
            break;
        case 3:
            result.textContent = 'тройка';
            break;
        case 4:
            result.textContent = 'четверка';
            break;
        case 5:
            result.textContent = 'пятерка';
            break;
        case 6:
            result.textContent = 'шестёрка';
            break;
        case 7:
            result.textContent = 'семёрка';
            break;
        case 8:
            result.textContent = 'восьмёрка';
            break;
        case 9:
            result.textContent = 'девятка';
            break;
        default:
            result.textContent = 'не цифра';
            break;
    }
});
