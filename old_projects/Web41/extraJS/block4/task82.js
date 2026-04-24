const prompt = require('prompt-sync')();

const firstNumber = parseInt(prompt("Введите первое целое число:"));
const secondNumber = parseInt(prompt("Введите второе целое число:"));
const thirdNumber = parseInt(prompt("Введите третье целое число:"));
const fourthNumber = parseInt(prompt("Введите четвертое целое число:"));


function isEven(num) {
    return num % 2 === 0;
}

const evenCount = 
    (isEven(firstNumber) ? 1 : 0) +
    (isEven(secondNumber) ? 1 : 0) +
    (isEven(thirdNumber) ? 1 : 0) +
    (isEven(fourthNumber) ? 1 : 0);

console.log(`Количество четных чисел: ${evenCount}`);