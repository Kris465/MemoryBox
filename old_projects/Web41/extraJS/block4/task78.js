const prompt = require('prompt-sync')();
const firstNumber = parseInt(prompt("Введите первое целое число:"));
const secondNumber = parseInt(prompt("Введите второе целое число:"));
const thirdNumber = parseInt(prompt("Введите третье целое число:"));

function isEven(num) {
    return num % 2 === 0;
}

let evenNumbers = [];

if (isEven(firstNumber)) {
    evenNumbers.push(firstNumber);
}
if (isEven(secondNumber)) {
    evenNumbers.push(secondNumber);
}
if (isEven(thirdNumber)) {
    evenNumbers.push(thirdNumber);
}

if (evenNumbers.length > 0) {
    console.log("Четные числа:", evenNumbers.join(", "));
} else {
    console.log("Нет четных чисел.");
}