const prompt = require('prompt-sync')();

let a = prompt('Введите значение a: ');
let b = (Math.pow(a, 2) + 10) / Math.sqrt(Math.pow(a, 2) + 1);
console.log(`Ответ: ${b}`);