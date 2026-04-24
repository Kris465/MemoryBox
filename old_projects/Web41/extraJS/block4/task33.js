const prompt = require('prompt-sync')();

function analyzeNumber(number) {
    if (number <= 0 || !Number.isInteger(number)) {
        console.log("Пожалуйста, введите натуральное число.");
        return;
    }
    const numStr = number.toString();
    const lastDigit = parseInt(numStr[numStr.length - 1]);
    const isEven = lastDigit % 2 === 0;
    console.log(`Число заканчивается четной цифрой: ${isEven}`);
    const isOdd = lastDigit % 2 !== 0;
    console.log(`Число заканчивается нечетной цифрой: ${isOdd}`);
}

let number = parseInt(prompt("Введите натуральное число:"));
if (!isNaN(number)) {
    analyzeNumber(number);
} else {
    console.log("Пожалуйста, введите корректное число.");
}