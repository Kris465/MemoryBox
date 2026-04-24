const prompt = require('prompt-sync')();

let continueCalc;

do {
    let num1 = Number(prompt("Введите первое число: "));
    let num2 = Number(prompt("Введите второе число: "));
    let symbol = prompt("Введите знак: ")

    let result;
    switch (symbol) {
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
            console.log('некоректные операции');
            continue;
    }

    console.log(`результат: ${result}`);
    continueCalc = prompt('Хотите решить еще один пример (y/n): ').toLowerCase();
} while (continueCalc == 'y');

