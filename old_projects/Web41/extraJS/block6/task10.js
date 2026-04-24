const prompt = require('prompt-sync')();
const n = parseInt(prompt("Введите число n:"));

console.log("Числа, квадраты которых не превышают n:");
for (let i = 1; i * i <= n; i++) {
    console.log(i);
}

let k = 1;
while (k * k <= n) {
    k++;
}
console.log("Первое натуральное число, квадрат которого больше n:", k);