const prompt = require('prompt-sync')();

let x = prompt('Введите значение х: ');
let y = 7*Math.pow(x, 2)-3*x+6

console.log(`Ответ: ${y}`);

let a = prompt('Введите значение a: ');
let b = 12*Math.pow(a, 2)+7*a-16;

console.log(`Ответ: ${b}`);