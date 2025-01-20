const prompt = require('prompt-sync')(); // Импортируем библиотеку prompt-sync

// Рекурсивная функция для нахождения максимальной цифры в числе
function findMaxDigit(num) {
    // Преобразуем число в строку, чтобы работать с каждой цифрой
    const strNum = num.toString();

    // Базовый случай: если длина строки равна 1, возвращаем единственную цифру
    if (strNum.length === 1) {
        return parseInt(strNum); // Преобразуем обратно в число
    }

    // Рекурсивный случай: сравниваем первую цифру с максимальной цифрой оставшейся части
    const firstDigit = parseInt(strNum[0]);
    const maxOfRest = findMaxDigit(strNum.slice(1)); // Рекурсивно обрабатываем оставшиеся цифры

    // Возвращаем максимальную из двух цифр
    return Math.max(firstDigit, maxOfRest);
}

// Получаем пользовательский ввод
const input = prompt('Введите число: ');

// Проверяем, является ли введенное значение числом
if (isNaN(input) || input.trim() === '') {
    console.log('Пожалуйста, введите корректное число.');
} else {
    const number = Math.abs(parseInt(input, 10)); // Берем абсолютное значение числа
    const maxDigit = findMaxDigit(number); // Вызываем рекурсивную функцию
    console.log(`Максимальная цифра в числе ${number} равна ${maxDigit}`);
}
