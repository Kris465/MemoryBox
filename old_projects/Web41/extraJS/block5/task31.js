const prompt = require('prompt-sync')();

function sumOfSquares(n) {
    let sum = 0;
    for (let i = n; i <= 2 * n; i++) {
        sum += Math.pow(i, 2);
    }
    return sum;
}

let n = parseInt(prompt("Введите натуральное число n:"));
if (n > 0) {
    let result = sumOfSquares(n);
    console.log(`Сумма квадратов от ${n} до ${2 * n}:`, result);
} else {
    console.log("Ошибка: n должно быть натуральным числом.");
}