const prompt = require('prompt-sync')();

// Функция для нахождения минимального значения
function findMinimum(...args) {
    return Math.min(...args);
}

// Функция для сбора чисел от пользователя
function collectNumbers() {
    const numbers = [];

    while (true) {
        const input = prompt('Введите число (или "стоп" для завершения): ');

        if (input.toLowerCase() === 'стоп') {
            break; // Выход из цикла, если введено "стоп"
        }

        const number = parseFloat(input); // Преобразуем ввод в число

        if (!isNaN(number)) {
            numbers.push(number); // Добавляем число в массив, если это действительно число
        } else {
            console.log('Пожалуйста, введите корректное число или "стоп".');
        }
    }

    // Возвращаем минимальное значение среди введенных чисел
    if (numbers.length > 0) {
        console.log(`Минимальное значение: ${findMinimum(...numbers)}`);
    } else {
        console.log('Не было введено ни одного числа.');
    }
}

// Запускаем сбор чисел
collectNumbers();
