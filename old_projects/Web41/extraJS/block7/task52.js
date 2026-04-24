const prompt = require('prompt-sync')();


const n = parseInt(prompt("Введите количество чисел:"));

const numbers = prompt(`Введите ${n} вещественных числа через пробел:`).split(' ').map(Number);

const maxNumber = Math.max(...numbers);
const minNumber = Math.min(...numbers);

console.log(`Максимальное число: ${maxNumber}`);
console.log(`Минимальное число: ${minNumber}`);