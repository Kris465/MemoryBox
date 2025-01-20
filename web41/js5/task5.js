const prompt = require('prompt-sync')(); // Импортируем библиотеку prompt-sync

function isPowerOfTwo(x) {
    if (x <= 0) {
        return false; // Неположительные числа не являются степенью двойки
    }
    if (x === 1) {
        return true; // 2^0 = 1
    }
    return isPowerOfTwo(x / 2); // Рекурсивно проверяем
}

// Получаем пользовательский ввод
const userInput = prompt('Введите число для проверки, является ли оно степенью двойки: ');

// Преобразуем введенное значение в число
const number = parseInt(userInput, 10);

// Проверяем, является ли введенное число степенью двойки и выводим результат
if (isNaN(number)) {
    console.log('Пожалуйста, введите корректное число.');
} else {
    const result = isPowerOfTwo(number);
    console.log(`${number} ${result ? 'является' : 'не является'} степенью двойки.`);
}
