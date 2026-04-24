const prompt = require('prompt-sync')();

const x = parseInt(prompt("Введите число x:"));
let sum = 0;
let countEven = 0;

while (true) {
    const num = parseInt(prompt("Введите число (0 для завершения):"));
    if (num === 0) break;
    if (num > x) {
        sum += num;
    }
    if (num % 2 === 0) {
        countEven++;
    }
}

console.log("а) Сумма чисел, больших x: " + sum);
console.log("б) Количество четных чисел: " + countEven);