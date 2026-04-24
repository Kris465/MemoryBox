const prompt = require('prompt-sync')();
let number1 = Number(prompt('Введите первое число: '));
let number2 = Number(prompt('Введите второе число: '));
let number3 = Number(prompt('Введите третье число: '));
let srednee = (number1 + number2 + number3) / 3;
console.log("Среднее арифметическое: " + srednee);