const prompt = require('prompt-sync')(); 

const numberStr = prompt("Введите натуральное число:");
const m = parseInt(prompt("Введите число m:"), 10);
const len = numberStr.length;
const start = len - m >= 0 ? len - m : 0;
let sum = 0;
for (let i = start; i < len; i++) {
    sum += parseInt(numberStr[i], 10);
}
console.log(`Сумма последних ${m} цифр: ${sum}`);