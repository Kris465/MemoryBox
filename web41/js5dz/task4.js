const prompt = require('prompt-sync')(); // Импортируем библиотеку prompt-sync

// Рекурсивная функция для проверки, является ли число простым
function isPrime(num, divisor = 2) {
    // Базовый случай: если num меньше 2, оно не простое
    if (num < 2) {
        return false;
    }
    // Если делитель стал больше квадратного корня из num, значит, num простое
    if (divisor * divisor > num) {
        return true;
    }
    // Если num делится на divisor, то оно не простое
    if (num % divisor === 0) {
        return false;
    }
    // Рекурсивный вызов с увеличенным делителем
    return isPrime(num, divisor + 1);
}

// Получаем пользовательский ввод
const input = prompt('Введите число: ');

// Проверяем, является ли введенное значение числом
if (isNaN(input) || input.trim() === '') {
    console.log('Пожалуйста, введите корректное число.');
} else {
    const number = Math.abs(parseInt(input, 10)); // Берем абсолютное значение числа
    const result = isPrime(number); // Вызываем рекурсивную функцию
    if (result) {
        console.log(`${number} является простым числом.`);
    } else {
        console.log(`${number} не является простым числом.`);
    }
}
