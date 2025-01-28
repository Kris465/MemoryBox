const prompt = require('prompt-sync')();

function findMaxDigit(num) {
    const strNum = num.toString();
    if (strNum.length === 1) {
        return parseInt(strNum);
    }
    const firstDigit = parseInt(strNum[0]);
    const maxOfRest = findMaxDigit(strNum.slice(1));

    return Math.max(firstDigit, maxOfRest);
}

const input = prompt('Введите число: ');

if (isNaN(input) || input.trim() === '') {
    console.log('Пожалуйста, введите корректное число.');
} else {
    const number = Math.abs(parseInt(input, 10));
    const maxDigit = findMaxDigit(number);
    console.log(`Максимальная цифра в числе ${number} равна ${maxDigit}`);
}
