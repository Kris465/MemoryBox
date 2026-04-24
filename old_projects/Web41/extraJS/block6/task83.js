const prompt = require('prompt-sync')(); 

const numStr = prompt("Введите натуральное число:");
const a = parseInt(prompt("Введите число a:"), 10);

let maxDigit = 0;
let minDigit = 9;

for (let digit of numStr) {
    const d = parseInt(digit, 10);
    if (d > maxDigit) maxDigit = d;
    if (d < minDigit) minDigit = d;
}

const sumDigits = maxDigit + minDigit;

if (sumDigits % a === 0) {
    console.log(`Сумма максимальной и минимальной цифр (${sumDigits}) кратна числу ${a}.`);
} else {
    console.log(`Сумма максимальной и минимальной цифр (${sumDigits}) не кратна числу ${a}.`);
}