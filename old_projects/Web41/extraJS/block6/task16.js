const prompt = require('prompt-sync')();

const target = parseFloat(prompt("Введите число n:"));
let sum = 0;
let i = 0;
while (true) {
    i++;
    sum += 1 / i;
    if (sum > target) {
        console.log(i);
        break;
    }
}
