const prompt = require('prompt-sync')();

function fibonacci(n) {
    if (n <= 0) {
        return 0;
    }
    if (n === 1 || n === 2) {
        return 1;
    }
    return fibonacci(n - 1) + fibonacci(n - 2);
}

const input = prompt('Введите порядковый номер числа Фибоначчи: ');

if (isNaN(input) || input.trim() === '') {
    console.log('Пожалуйста, введите корректное число.');
} else {
    const number = parseInt(input, 10);
    const result = fibonacci(number);
    console.log(`Число Фибоначчи с порядковым номером ${number}: ${result}`);
}
