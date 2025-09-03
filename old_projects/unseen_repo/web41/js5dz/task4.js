const prompt = require('prompt-sync')();

function isPrime(num, divisor = 2) {
    if (num < 2) {
        return false;
    }
    if (divisor * divisor > num) {
        return true;
    }
    if (num % divisor === 0) {
        return false;
    }
    return isPrime(num, divisor + 1);
}
const input = prompt('Введите число: ');

if (isNaN(input) || input.trim() === '') {
    console.log('Пожалуйста, введите корректное число.');
} else {
    const number = Math.abs(parseInt(input, 10));
    const result = isPrime(number);
    if (result) {
        console.log(`${number} является простым числом.`);
    } else {
        console.log(`${number} не является простым числом.`);
    }
}
