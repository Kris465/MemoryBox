const prompt = require('prompt-sync')(); 

const numberStr = prompt("Введите натуральное число, в котором все цифры различны:");
const digits = numberStr.split('');
const len = digits.length;

let maxDigit = -1;
let minDigit = 10;
let maxIndexFromStart = -1;
let minIndexFromStart = -1;

for (let i = 0; i < len; i++) {
    const d = parseInt(digits[i]);
    if (d > maxDigit) {
        maxDigit = d;
        maxIndexFromStart = i + 1; 
    }
    if (d < minDigit) {
        minDigit = d;
        minIndexFromStart = i + 1;
    }
}

const maxIndexFromEnd = len - maxIndexFromStart + 1;
const minIndexFromEnd = len - minIndexFromStart + 1;

console.log("а) Порядковый номер максимальной цифры от начала: " + maxIndexFromStart);
console.log("а) Порядковый номер максимальной цифры от конца: " + maxIndexFromEnd);
console.log("б) Порядковый номер минимальной цифры от начала: " + minIndexFromStart);
console.log("б) Порядковый номер минимальной цифры от конца: " + minIndexFromEnd);