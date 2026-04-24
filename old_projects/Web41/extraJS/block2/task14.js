const prompt = require('prompt-sync')();

const num = prompt("введите 3х-значное число: ");

if (num < 100 || num > 999) {
    console.log("Ошибка: число должно быть трехзначным.");
} else {
    const numStr = num.toString();
    
    const firstDigit = numStr.charAt(0);
    const lastTwoDigits = numStr.slice(1);
    
    const newNumStr = lastTwoDigits + firstDigit;
    const newNum = parseInt(newNumStr);
    
    console.log(`Новое число: ${newNum}`);
}