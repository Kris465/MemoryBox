const prompt = require('prompt-sync')();

const num = prompt("введите 3х значное число: ");

const hundreds = Math.floor(num / 100); 
const tens = Math.floor((num % 100) / 10); 
const units = num % 10;

const sum = hundreds + tens + units;  
const product = hundreds * tens * units;  

console.log(`Число единиц: ${units}`);
console.log(`Число десятков: ${tens}`);
console.log(`Сумма цифр: ${sum}`);
console.log(`Произведение цифр: ${product}`);
