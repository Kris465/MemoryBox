const prompt = require('prompt-sync')();

function compareNambers(num1, num2) {
    if (num1 > num2) {
        return 1;

    } else if (num1 < num2) {
        return -1;
        
    } else {
        return 0;
    }
}

let num1 = prompt('Введите первое число');
let num2 = prompt('Введите второе число');
const result = compareNambers(num1, num2);
console.log(`результат сравнение: ${result}`);

