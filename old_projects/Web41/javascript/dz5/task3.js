const prompt = require('prompt-sync')();

function findMaxDigit(num) {
    const digits = num.toString();
    let maxDigit = 0;

    for (let digit of digits) {
        const digitNum = Number(digit);
        if (digitNum > maxDigit) {
            maxDigit = digitNum;
        }
    }

    return maxDigit;
}

const num1 = prompt("Введите число: ");

console.log(`ответ ${findMaxDigit(num1)}`);