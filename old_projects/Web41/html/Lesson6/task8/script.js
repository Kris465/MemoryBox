const prompt = require('prompt-sync')();
let number1 = Number(prompt('Введите первое число: '));
let number2 = Number(prompt('Введите второе число: '));
let max;
if (number1 > number2) {
    max = number1
} else {
    max = number2
}
console.log("Наибольшее число: " + max);