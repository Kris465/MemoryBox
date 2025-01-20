const prompt = require('prompt-sync')(); // Импортируем библиотеку prompt-sync

// Рекурсивная функция для возведения числа в степень
function power(base, exponent) {
    // Базовый случай: любое число в степени 0 равно 1
    if (exponent === 0) {
        return 1;
    }
    // Если степень отрицательная, используем обратное значение
    if (exponent < 0) {
        return 1 / power(base, -exponent);
    }
    // Рекурсивный случай: base * power(base, exponent - 1)
    return base * power(base, exponent - 1);
}

// Получаем пользовательский ввод для основания и степени
const baseInput = prompt('Введите основание (число): ');
const exponentInput = prompt('Введите степень (целое число): ');

// Преобразуем введенные значения в числа
const base = parseFloat(baseInput);
const exponent = parseInt(exponentInput, 10);

// Проверяем, является ли основание числом и степень целым числом
if (isNaN(base) || isNaN(exponent)) {
    console.log('Пожалуйста, введите корректные числа.');
} else {
    // Вызываем функцию и выводим результат
    const result = power(base, exponent);
    console.log(`${base} в степени ${exponent} равно ${result}`);
}
