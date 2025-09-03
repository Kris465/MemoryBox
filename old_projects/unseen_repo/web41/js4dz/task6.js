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

// Функция для нахождения совершенных чисел в диапазоне
function findPerfectNumbersInRange(min, max) {
    console.log(`Совершенные числа в диапазоне от ${min} до ${max}:`);
    for (let num = min; num <= max; num++) {
        if (isPerfectNumber(num)) {
            console.log(num);
        }
    }
}

// Получаем ввод от пользователя
const minInput = prompt('Введите минимальное значение диапазона: ');
const maxInput = prompt('Введите максимальное значение диапазона: ');

// Преобразуем ввод в числа
const min = parseInt(minInput, 10);
const max = parseInt(maxInput, 10);

// Проверяем, что минимальное значение меньше максимального
if (min >= max) {
    console.log('Минимальное значение должно быть меньше максимального.');
} else {
    // Ищем совершенные числа в заданном диапазоне
    findPerfectNumbersInRange(min, max);
}
