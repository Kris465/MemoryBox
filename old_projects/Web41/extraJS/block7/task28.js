const prompt = require('prompt-sync')();

const n = parseInt(prompt("Введите натуральное число n:"), 10);
const p = parseInt(prompt("Введите число p:"), 10);
const k = parseInt(prompt("Введите число k:"), 10);
let countGreaterP = 0;
let countEndingWith5 = 0;
let countDivisibleK = 0;

for (let i = 0; i < n; i++) {
    const a = parseInt(prompt(`Введите число a${i + 1}:`), 10);
    if (a > p) {
        countGreaterP++;
    }
    if (Math.abs(a) % 10 === 5) {
        countEndingWith5++;
    }
    if (a % k === 0) {
        countDivisibleK++;
    }
}

console.log("Количество чисел больше p:", countGreaterP);
console.log("Количество чисел, оканчивающихся цифрой 5:", countEndingWith5);
console.log("Количество чисел, кратных k:", countDivisibleK);