const prompt = require('prompt-sync')(); 

const numberStr = prompt("Введите натуральное число:");
let maxDigit = -1;
let minDigit = 10;

for (let digit of numberStr) {
    const d = parseInt(digit);
    if (d > maxDigit) maxDigit = d;
    if (d < minDigit) minDigit = d;
}

const difference = maxDigit - minDigit;
const sumDigits = maxDigit + minDigit;

console.log("а) Максимальная цифра: " + maxDigit);
console.log("а) Минимальная цифра: " + minDigit);
console.log("б) Разница между максимальной и минимальной цифрой: " + difference);
console.log("в) Сумма максимальной и минимальной цифр: " + sumDigits);