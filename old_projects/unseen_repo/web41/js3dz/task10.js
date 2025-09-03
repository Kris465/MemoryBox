const prompt = require('prompt-sync')();

let min = 0;
let max = 100;
let guess;
let response;

console.log("Загадайте число от 0 до 100, а я постараюсь его угадать!");

do {
    guess = Math.floor((min + max) / 2); // Находим среднее значение
    response = prompt(`Ваше число > ${guess}, < ${guess} или == ${guess}? (введите '>', '<' или '=='): `);

    if (response === '>') {
        min = guess + 1; // Увеличиваем нижнюю границу
    } else if (response === '<') {
        max = guess - 1; // Уменьшаем верхнюю границу
    } else if (response !== '==') {
        console.log("Пожалуйста, введите только '>', '<' или '=='.");
    }
} while (response !== '==');

console.log(`Ура! Я угадал ваше число: ${guess}`);
