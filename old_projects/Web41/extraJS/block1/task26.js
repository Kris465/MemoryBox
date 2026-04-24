const prompt = require('prompt-sync')();

let R = prompt('Введите значение радиуса: ');
let D = 2 * R

console.log(`Диаметр равен: ${D}`);