const prompt = require('prompt-sync')();

const a = parseFloat(prompt("Введите число a:"));
const x = parseFloat(prompt("Введите число x:"));
let y_prev = 1;
let y_curr = 1 / x;
let n = 1;

while (true) {
    if (n > 1 && Math.pow(y_curr, 2) - Math.pow(y_prev, 2) <= a) {
        console.log(`Первый член n: ${n}, y: ${y_curr}`);
        break;
    }
    y_prev = y_curr;
    n++;
    y_curr = y_prev / x;
}