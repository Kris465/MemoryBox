const prompt = require('prompt-sync')();

function findFactors(num, divisor = 2) {
    if (num === 1) {
        return [];
    }

    if (num % divisor === 0) {
        return [divisor].concat(findFactors(num / divisor, divisor));
    } else {
        return findFactors(num, divisor + 1);
    }
}


const input = prompt('Введите число: ');


if (isNaN(input) || input.trim() === '') {
    console.log('Пожалуйста, введите корректное число.');
} else {
    const number = Math.abs(parseInt(input, 10));
    const factors = findFactors(number);
    console.log(`Множители числа ${number}: ${factors.join(' * ')}`);
}
