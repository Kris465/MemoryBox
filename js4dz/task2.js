const prompt = require('prompt-sync')();

function factorial(n) {
    // Проверяем, является ли n отрицательным числом
    if (n < 0) {
        return 'Факториал не определен для отрицательных чисел';
    }
    // Факториал 0 равен 1
    if (n === 0) {
        return 1;
    }
    // Вычисляем факториал с помощью рекурсии
    return n * factorial(n - 1);
}

// Пример использования
const number = parseInt(prompt('Введите число для вычисления факториала: '));
const result = factorial(number);
console.log(`Факториал ${number} равен ${result}`);
