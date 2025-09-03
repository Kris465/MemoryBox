const prompt = require('prompt-sync')();

// Функция для проверки, является ли число совершенным
function isPerfectNumber(num) {
    if (num <= 1) return false; // Совершенные числа начинаются с 6

    let sum = 0;
    for (let i = 1; i <= num / 2; i++) { // Проверяем делители до num/2
        if (num % i === 0) {
            sum += i; // Добавляем делитель к сумме
        }
    }
    return sum === num; // Проверяем, равна ли сумма числу
}

// Получаем ввод от пользователя
const userInput = prompt('Введите число для проверки: ');

// Преобразуем ввод в число
const number = parseInt(userInput, 10);

// Проверяем, является ли число совершенным и выводим результат
if (isPerfectNumber(number)) {
    console.log(`${number} является совершенным числом.`);
} else {
    console.log(`${number} не является совершенным числом.`);
}
