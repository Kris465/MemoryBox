const prompt = require('prompt-sync')();

const n = parseInt(prompt("Введите число n (больше 1):"));
let a = 1;
let b = 1;

while (b <= n) {
    const next = a + b;
    a = b;
    b = next;
}
console.log(`Первое число в последовательности Фибоначчи, большее n: ${b}`);

let sum = 0;
a = 1;
b = 1;

while (a <= 1000) {
    sum += a;
    const next = a + b;
    a = b;
    b = next;
}
console.log(`Сумма чисел Фибоначчи, не превосходящих 1000: ${sum}`);