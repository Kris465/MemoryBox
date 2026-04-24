const prompt = require('prompt-sync')();

const num = prompt("введите 3х-значное число: ");

if (num < 100 || num > 999) {
    console.log("Ошибка: число должно быть трехзначным.");
} else {
    const numStr = num.toString();

    const lastDigit = numStr.charAt(2); 
    const firstTwoDigits = numStr.slice(0, 2); 

    const newNumStr = lastDigit + firstTwoDigits; 
    const result = parseInt(newNumStr); 

    console.log(`Новое число: ${result}`);
}