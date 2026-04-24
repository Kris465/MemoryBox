const prompt = require('prompt-sync')();

const n = parseInt(prompt("Введите количество чисел в последовательности:"), 10);
const sequence = [];
for (let i = 0; i < n; i++) {
    sequence.push(parseFloat(prompt(`Введите число ${i + 1}:`)));
}
let countNegatives = 0;
for (let num of sequence) {
    const isNegative = num < 0;
    countNegatives += isNegative * 1;
    const continueLoop = !isNegative;
    if (!continueLoop) break;
}
console.log("Количество отрицательных чисел в начале последовательности:", countNegatives);