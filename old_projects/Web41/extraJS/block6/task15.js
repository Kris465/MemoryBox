const prompt = require('prompt-sync')();

const a = parseFloat(prompt("Введите вещественное число a:"));
let n = 1;
while (true) {
    const current = 1 + 1 / n;
    if (current >= a) {
        break;
    }
    console.log(current);
    n++;
}