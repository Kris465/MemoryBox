const prompt = require('prompt-sync')();

let a = parseInt(prompt("Введите двузначное число: "));
let b = parseInt(prompt("Введите однозначное число : "));

let sum = a + b;

let tens = Math.floor(sum / 10); 
let units = sum % 10;

console.log(`Сумма: ${sum}`);
console.log(`Десятки: ${tens}, Единицы: ${units}`);