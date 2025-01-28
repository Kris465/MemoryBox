const prompt = require('prompt-sync')();

function power(base, exponent) {
    if (exponent === 0) {
        return 1;
    }
    if (exponent < 0) {
        return 1 / power(base, -exponent);
    }
    return base * power(base, exponent - 1);
}

const baseInput = prompt('Введите основание (число): ');
const exponentInput = prompt('Введите степень (целое число): ');

const base = parseFloat(baseInput);
const exponent = parseInt(exponentInput, 10);

if (isNaN(base) || isNaN(exponent)) {
    console.log('Пожалуйста, введите корректные числа.');
} else {
    const result = power(base, exponent);
    console.log(`${base} в степени ${exponent} равно ${result}`);
}
