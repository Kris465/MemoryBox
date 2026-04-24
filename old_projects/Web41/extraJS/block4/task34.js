const prompt = require('prompt-sync')();

function checkDivisibility(a, b) {

    if (a <= 0 || b <= 0) {
        console.log("Пожалуйста, введите натуральные числа больше нуля.");
        return;
    }

    const isADivisorOfB = b % a === 0;
    console.log(`Число ${a} является делителем числа ${b}: ${isADivisorOfB}`);

    const isBDivisorOfA = a % b === 0;
    console.log(`Число ${b} является делителем числа ${a}: ${isBDivisorOfA}`);
}

let a = parseInt(prompt("Введите число a:"));
let b = parseInt(prompt("Введите число b:"));
if (!isNaN(a) && !isNaN(b)) {
    checkDivisibility(a, b);
} else {
    console.log("Пожалуйста, введите корректные числа.");
}