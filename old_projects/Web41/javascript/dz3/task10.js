const prompt = require('prompt-sync')();
let min = 0;
let max = 100;
let guess;
let response;

console.log("загадайте число от 1 до 100");
do {
    guess = Math.floor((min + max) / 2);
    response = prompt(`ваше число > ${guess} или == ${guess}, < ${guess} или == ${guess}? (введите '>','<' или '=='); `);
    if (response === '>') {
        min = guess + 1; 
        
    } else if  (response === '<') {
        max = guess - 1;

    } else if (response !== '==') {
        console.log("пожалуйста введите только '>', '<' или '=='.");
    }
} while (response !== '==');
console.log(`я угадал ваше число: ${guess}`);
