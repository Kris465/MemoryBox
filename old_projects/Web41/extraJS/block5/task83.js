const prompt = require('prompt-sync')();

function power(a, n) {
    let result = 1;
    for (let i = 0; i < n; i++) {
        result *= a;
    }
    return result;
}

const userInputA = prompt("Введите вещественное число a:");
const userInputN = prompt("Введите натуральное число n:");

const a = parseFloat(userInputA);
const n = parseInt(userInputN);

if (!isNaN(a) && !isNaN(n) && n > 0) {
    const result = power(a, n);
    console.log(`${a} в степени ${n} равно ${result}`);
} else {
    console.log("Пожалуйста, введите корректные значения: вещественное число для a и натуральное число для n.");
}