const prompt = require('prompt-sync')();

function factorial(n) {
    if (n === 0 || n === 1) {
        return 1;
    }
    let result = 1;
    for (let i = 2; i <= n; i++) {
        result *= i;
    }
    return result;
}

const userInput = prompt("Введите натуральное число n:");
const n = parseInt(userInput);

if (!isNaN(n) && n > 0) {
    const fact = factorial(n);
    console.log(`Факториал числа ${n} равен ${fact}`);
} else {
    console.log("Пожалуйста, введите корректное натуральное число.");
}