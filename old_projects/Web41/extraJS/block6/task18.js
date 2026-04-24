const prompt = require('prompt-sync')();

const a = parseFloat(prompt("Введите вещественное число a:"));
let sum = 0;
let n = 0;
while (true) {
    n++;
    sum += 1 / n;
    if (sum > a) {
        console.log(n);
        break;
    }
}