const prompt = require('prompt-sync')();

const n = parseInt(prompt("Введите натуральное число n:"), 10);
const p = parseFloat(prompt("Введите число p:"));

let sum = 0;

for (let i = 1; i <= n; i++) {
    const input = prompt(`Введите вещественное число ${i}:`);
    const num = parseFloat(input);
    if (num > p) {
        sum += num;
    }
}

console.log(`Сумма чисел, больших ${p}:`, sum);