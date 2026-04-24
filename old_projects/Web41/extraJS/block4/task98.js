const prompt = require('prompt-sync')();

function findMaxMin(a, b, c) {
    let max, min;

    if (a > b && a > c) {
        max = a;
    } else if (b > a && b > c) {
        max = b;
    } else {
        max = c;
    }

    if (a < b && a < c) {
        min = a;
    } else if (b < a && b < c) {
        min = b;
    } else {
        min = c;
    }

    return {
        max: max,
        min: min
    };
}

const num1 = parseFloat(prompt("Введите первое вещественное число:"));
const num2 = parseFloat(prompt("Введите второе вещественное число:"));
const num3 = parseFloat(prompt("Введите третье вещественное число:"));

if (num1 === num2 || num1 === num3 || num2 === num3) {
    console.log("Числа должны быть различными.");
} else {
    const result = findMaxMin(num1, num2, num3);
    
    console.log(`Максимальное значение: ${result.max}`);
    console.log(`Минимальное значение: ${result.min}`);
}