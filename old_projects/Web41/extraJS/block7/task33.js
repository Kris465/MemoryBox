const prompt = require('prompt-sync')();

const n = parseInt(prompt("Введите количество чисел:"));
let positiveCount = 0;
let negativeCount = 0;

for (let i = 0; i < n; i++) {
    const num = parseFloat(prompt(`Введите число ${i + 1}:`));
    if (num > 0) {
        positiveCount++;
    } else if (num < 0) {
        negativeCount++;
    }
}

console.log(`Количество положительных чисел: ${positiveCount}`);
console.log(`Количество отрицательных чисел: ${negativeCount}`);