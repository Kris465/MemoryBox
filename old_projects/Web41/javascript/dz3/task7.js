const prompt = require('prompt-sync')();
let num1 = prompt('введите число: ');
let shift = prompt('введите число на которое сметить: ');

shift %= num1.length;
let result = num1.slice(shift) + num1.slice(0, shift);
console.log(`результат сдвига: ${result}`);