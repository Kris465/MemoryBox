const prompt = require('prompt-sync')();

let a = prompt('Введите значение a: ');
let x = prompt('Введите значение x: ');

let b = (Math.sqrt(2 * a + Math.sin(Math.abs(3 * a) * Math.PI / 180) / 3.56));
let c = (Math.sin(3.2 + Math.sqrt(1 + x) / Math.abs(5 * x) * Math.PI / 180));

console.log(`Ответ: ${b}`);
console.log(`Ответ: ${c} `);