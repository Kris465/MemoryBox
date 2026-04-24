const prompt = require('prompt-sync')();

const firstNumber = parseFloat(prompt("Введите первое вещественное число:"));
const secondNumber = parseFloat(prompt("Введите второе вещественное число:"));
const thirdNumber = parseFloat(prompt("Введите третье вещественное число:"));
const fourthNumber = parseFloat(prompt("Введите четвертое вещественное число:"));

function isGreaterThanFive(num) {
    return num > 5;
}

const sum = 
    (isGreaterThanFive(firstNumber) ? firstNumber : 0) +
    (isGreaterThanFive(secondNumber) ? secondNumber : 0) +
    (isGreaterThanFive(thirdNumber) ? thirdNumber : 0) +
    (isGreaterThanFive(fourthNumber) ? fourthNumber : 0);

console.log(`Сумма чисел больше 5: ${sum}`);