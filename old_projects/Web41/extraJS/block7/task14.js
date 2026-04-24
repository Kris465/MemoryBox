const prompt = require('prompt-sync')();
let sum = 0;

for (let i = 1; i <= 8; i++) {
    const input = prompt(`Введите вещественное число ${i}:`);
    const num = parseFloat(input);
    if (num > 10.75) {
        sum += num;
    }
}

console.log("Сумма чисел, больших 10.75:", sum);