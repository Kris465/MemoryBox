const prompt = require('prompt-sync')();
let num1 = Number(prompt("Введите первое число: "));
let num2 = Number(prompt("Введите второе число: "));

while (num2 != 0) {
    let temp = num2;
    num2 = num1 % num2;
    num1 = temp;
}
console.log(`нод равен ${num1}`);