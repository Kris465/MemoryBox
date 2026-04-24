const prompt = require('prompt-sync')();

const number = parseFloat(prompt("Введите вещественное число:"));


const absoluteValue = (number * (number >= 0) + -number * (number < 0));


console.log(`Абсолютная величина числа ${number} равна ${absoluteValue}`);