const prompt = require('prompt-sync')();

// Функция для вычисления площади
function calculateArea(length, width) {
    if (width === undefined) {
        return length * length; // Площадь квадрата
    } else {
        return length * width; // Площадь прямоугольника
    }
}

// Ввод длины
const length = parseFloat(prompt('Введите длину: '));

// Запрос на ввод ширины (можно оставить пустым для квадрата)
const widthInput = prompt('Введите ширину (нажмите Enter для квадрата): ');

// Проверяем, введена ли ширина
let width;
if (widthInput === '') {
    width = undefined; // Если ничего не введено, устанавливаем width как undefined
} else {
    width = parseFloat(widthInput); // Преобразуем ввод в число
}

// Вычисляем площадь
const area = calculateArea(length, width);

// Выводим результат
if (width === undefined) {
    console.log(`Площадь квадрата со стороной ${length}: ${area}`);
} else {
    console.log(`Площадь прямоугольника с длиной ${length} и шириной ${width}: ${area}`);
}
