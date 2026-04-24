const prompt = require('prompt-sync')();
let number1 = Number(prompt('Введите длину прямоугольника: '));
let number2 = Number(prompt('Введите ширину прямоугольника: '));
let perimeter = 2 * (number1 + number2);
console.log("Периметр прямоугольника: " + perimeter);
