const prompt = require('prompt-sync')(); 

const numberStr = prompt("Введите натуральное число:");
const digits = numberStr.split('').map(Number);
const length = digits.length;

let sum1 = 0;
let sum2 = 0;

for (let i = 0; i < length; i++) {
    const sign1 = (i % 2 === 0) ? 1 : -1;
    const sign2 = (i % 2 === 0) ? -1 : 1;
    sum1 += sign1 * digits[i];
    sum2 += sign2 * digits[i];
}

console.log("Знакочередующаяся сумма цифр числа (0, 1, ..., 1): " + sum1);
console.log("Знакочередующаяся сумма цифр числа (1, ..., 1, 0): " + sum2);