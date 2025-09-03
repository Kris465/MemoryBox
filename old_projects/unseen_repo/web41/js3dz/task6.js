const prompt = require('prompt-sync')();

let continueCalc;

do {
    let num1 = parseFloat(prompt('Введите первое число: '));
    let num2 = parseFloat(prompt('Введите второе число: '));
    let operation = prompt('Введите операцию (+, -, *, /): ');

    let result;
    switch (operation) {
        case '+':
            result = num1 + num2;
            break;
        case '-':
            result = num1 - num2;
            break;
        case '*':
            result = num1 * num2;
            break;
        case '/':
            result = num1 / num2;
            break;
        default:
            console.log('Некорректная операция');
            continue; // Если операция некорректная, повторяем цикл
    }

    console.log(`Результат: ${result}`);
    continueCalc = prompt('Хотите решить еще один пример? (y/n): ').toLowerCase();
} while (continueCalc === 'y');
