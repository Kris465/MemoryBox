const prompt = require('prompt-sync')();

function findMaxMin(a, b, c) {

    const maxAB = (a > b) ? a : b;
    const max = (maxAB > c) ? maxAB : c;

    const minAB = (a < b) ? a : b; 
    const min = (minAB < c) ? minAB : c;

    return { max, min };
}

const num1 = parseFloat(prompt("Введите первое вещественное число:"));
const num2 = parseFloat(prompt("Введите второе вещественное число:"));
const num3 = parseFloat(prompt("Введите третье вещественное число:"));

if (num1 !== num2 && num1 !== num3 && num2 !== num3) {
    const result = findMaxMin(num1, num2, num3);
    console.log(`Наибольшее: ${result.max}, Наименьшее: ${result.min}`);
} else {
    console.log("Числа должны быть различными. Пожалуйста, попробуйте снова.");
}