const prompt = require('prompt-sync')();

const firstNumber = parseInt(prompt("Введите первое целое число:"));
const secondNumber = parseInt(prompt("Введите второе целое число:"));
const thirdNumber = parseInt(prompt("Введите третье целое число:"));
const fourthNumber = parseInt(prompt("Введите четвертое целое число:"));

function isMultipleOfThree(num) {
    return num % 3 === 0; 
}

const sum = 
    (isMultipleOfThree(firstNumber) ? firstNumber : 0) +
    (isMultipleOfThree(secondNumber) ? secondNumber : 0) +
    (isMultipleOfThree(thirdNumber) ? thirdNumber : 0) +
    (isMultipleOfThree(fourthNumber) ? fourthNumber : 0);

console.log(`Сумма чисел, кратных 3: ${sum}`);