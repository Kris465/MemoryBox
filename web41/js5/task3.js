const prompt = require('prompt-sync')(); // Подключаем библиотеку prompt-sync

// Функция для подсчета количества числовых аргументов
function numbers(...args) {
    let count = 0; // Счетчик числовых аргументов

    // Проходим по всем аргументам и проверяем их тип
    for (const arg of args) {
        if (typeof arg === 'number') {
            count++; // Увеличиваем счетчик, если аргумент - число
        }
    }

    return count; // Возвращаем количество числовых аргументов
}

// Основная логика программы
function main() {
    const inputs = []; // Массив для хранения вводимых значений

    console.log("Введите числа (для завершения ввода введите 'exit'):");

    while (true) {
        const input = prompt('> '); // Запрашиваем ввод пользователя

        if (input.toLowerCase() === 'exit') {
            break; // Завершаем ввод, если пользователь ввел 'exit'
        }

        const number = parseFloat(input); // Пробуем преобразовать ввод в число

        if (!isNaN(number)) {
            inputs.push(number); // Если это число, добавляем его в массив
        } else {
            console.log("Пожалуйста, введите число или 'exit' для завершения."); // Сообщение об ошибке
        }
    }

    const count = numbers(...inputs); // Вызываем функцию numbers с введенными значениями
    console.log(`Количество введенных чисел: ${count}`); // Выводим результат
}

// Запускаем основную функцию
main();
