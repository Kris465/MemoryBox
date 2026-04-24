const prompt = require('prompt-sync')();

const firstNumber = parseFloat(prompt("Введите первое вещественное число:"));
const secondNumber = parseFloat(prompt("Введите второе вещественное число:"));
const thirdNumber = parseFloat(prompt("Введите третье вещественное число:"));
const fourthNumber = parseFloat(prompt("Введите четвертое вещественное число:"));


function isNegative(num) {
    return num < 0;
}


const negativeCount = 
    (isNegative(firstNumber) ? 1 : 0) +
    (isNegative(secondNumber) ? 1 : 0) +
    (isNegative(thirdNumber) ? 1 : 0) +
    (isNegative(fourthNumber) ? 1 : 0);


console.log(`Количество отрицательных чисел: ${negativeCount}`);