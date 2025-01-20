const prompt = require('prompt-sync')(); // Импортируем библиотеку prompt-sync

// Рекурсивная функция для нахождения множителей
function findFactors(num, divisor = 2) {
    // Если num равен 1, прекращаем рекурсию
    if (num === 1) {
        return [];
    }

    // Если num делится на divisor, добавляем divisor в массив и продолжаем с уменьшенным num
    if (num % divisor === 0) {
        return [divisor].concat(findFactors(num / divisor, divisor));
    } else {
        // Если не делится, пробуем следующий делитель
        return findFactors(num, divisor + 1);
    }
}

// Получаем пользовательский ввод
const input = prompt('Введите число: ');

// Проверяем, является ли введенное значение числом
if (isNaN(input) || input.trim() === '') {
    console.log('Пожалуйста, введите корректное число.');
} else {
    const number = Math.abs(parseInt(input, 10)); // Берем абсолютное значение числа
    const factors = findFactors(number); // Вызываем рекурсивную функцию
    console.log(`Множители числа ${number}: ${factors.join(' * ')}`);
}
