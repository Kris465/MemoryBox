const prompt = require('prompt-sync')();
let number1 = Number(prompt('Введите первое число: '));
let number2 = Number(prompt('Введите второе число: '));
let number3 = Number(prompt('Введите третье число: '));
let min;
if (number1 < number2 && number1 < number3) {
    min = number1
} else if (number2 < number1 && number2 < number3) {
    min = number2
} else {
    min = number3;
}
console.log("Наибольшее число: " + min);