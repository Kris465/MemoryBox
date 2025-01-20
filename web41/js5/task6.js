const prompt = require('prompt-sync')(); // Импортируем библиотеку prompt-sync

// Рекурсивная функция для вывода числа справа налево
function reverseNumber(n) {
    // Базовый случай: если n меньше 10, просто выводим его
    if (n < 10) {
        return n.toString(); // Преобразуем число в строку
    }
    
    // Рекурсивный вызов: получаем последнюю цифру и добавляем её к результату
    return (n % 10).toString() + reverseNumber(Math.floor(n / 10));
}

// Получаем пользовательский ввод
const userInput = prompt('Введите число для вывода справа налево: ');

// Преобразуем введенное значение в число
const number = parseInt(userInput, 10);

// Проверяем, является ли введенное значение числом
if (isNaN(number)) {
    console.log('Пожалуйста, введите корректное число.');
} else {
    // Вызываем функцию и выводим результат
    const reversed = reverseNumber(number);
    console.log(`Число ${number} справа налево: ${reversed}`);
}
