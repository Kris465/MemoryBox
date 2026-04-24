const prompt = require('prompt-sync')();

function areAllDigitsDifferent(n) {
    const numberStr = n.toString().padStart(4, '0');

    const uniqueDigits = new Set();

    for (let digit of numberStr) {
        uniqueDigits.add(digit);
    }

    return uniqueDigits.size === 4;
}

const input = prompt("Введите натуральное число (n <= 9999):");
const n = parseInt(input);

if (isNaN(n) || n < 0 || n > 9999) {
    console.log("Пожалуйста, введите корректное натуральное число от 0 до 9999.");
} else {
    const result = areAllDigitsDifferent(n);
    console.log(`В числе ${n} все цифры ${result ? "различны." : "не различны."}`);
}