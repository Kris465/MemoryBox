const prompt = require('prompt-sync')();
let number1 = Number(prompt('Введите первое число: '));
let number2 = Number(prompt('Введите второе число: '));
let stepen = number1 ** number2;
console.log("Возведение в степень: " + stepen);