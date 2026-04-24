const prompt = require('prompt-sync')();

const firstNumber = parseFloat(prompt("Введите первое вещественное число:"));
const secondNumber = parseFloat(prompt("Введите второе вещественное число:"));
const thirdNumber = parseFloat(prompt("Введите третье вещественное число:"));

function squareIfNonNegative(num) {
    return num >= 0 ? num * num : num; 
}

const squaredFirst = squareIfNonNegative(firstNumber);
const squaredSecond = squareIfNonNegative(secondNumber);
const squaredThird = squareIfNonNegative(thirdNumber);

console.log(`Результаты:`);
console.log(`Первое число: ${squaredFirst}`);
console.log(`Второе число: ${squaredSecond}`);
console.log(`Третье число: ${squaredThird}`);