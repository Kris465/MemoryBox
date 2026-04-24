const prompt = require('prompt-sync')();
let s = prompt('введите расстояние: ');
let t = prompt('введите время: ');
let result = s / t 
console.log(`ваша скорость ${result}`);
