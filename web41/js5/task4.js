const prompt = require('prompt-sync')(); // Подключаем библиотеку prompt-sync

// Функция для вычисления среднего значения
function mean(...args) {
    let sum = 0; // Сумма чисел
    let count = 0; // Количество чисел

    // Проходим по всем аргументам и проверяем их тип
    for (const arg of args) {
        if (typeof arg === 'number') {
            sum += arg; // Добавляем к сумме, если аргумент - число
            count++; // Увеличиваем счетчик чисел
        }
    }

    // Если чисел нет, возвращаем 0, иначе возвращаем среднее
    return count === 0 ? 0 : sum / count;
}

// Основная логика программы
function main() {
    const inputs = []; // Массив для хранения вводимых значений

    console.log("Введите значения (для завершения ввода введите 'exit'):");

    while (true) {
        const input = prompt('> '); // Запрашиваем ввод пользователя

        if (input.toLowerCase() === 'exit') {
            break; // Завершаем ввод, если пользователь ввел 'exit'
        }

        // Пробуем преобразовать ввод в число
        const number = parseFloat(input);

        // Если это число, добавляем его в массив, иначе добавляем строку
        if (!isNaN(number)) {
            inputs.push(number);
        } else {
            inputs.push(input); // Добавляем нечисловое значение в массив
        }
    }

    const average = mean(...inputs); // Вызываем функцию mean с введенными значениями
    console.log(`Среднее значение введенных чисел: ${average}`); // Выводим результат
}

// Запускаем основную функцию
main();
