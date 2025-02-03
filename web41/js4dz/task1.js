const prompt = require('prompt-sync')();

function compareNumbers(num1, num2) {
    if (num1 < num2) {
        return -1;
    } else if (num1 > num2) {
        return 1;
    } else {
        return 0;
    }
}

const number1 = parseFloat(prompt('Введите первое число: '));
const number2 = parseFloat(prompt('Введите второе число: '));

const result = compareNumbers(number1, number2);
console.log(`Результат сравнения: ${result}`);
