const prompt = require('prompt-sync')();

function calculateSum(x) {

    const numbers = [2, 3, 10, 2, 3, 4, 11, 1, 3, 4, 5, 12];
    let sum = 0;

    for (let i = 0; i < numbers.length; i++) {
        sum += numbers[i];
    }

    let totalSum = sum * x;

    return totalSum;
}

let x = parseInt(prompt("Введите количество повторений x:"));
if (x > 0) {
    let result = calculateSum(x);
    console.log("Сумма:", result);
} else {
    console.log("Ошибка: x должно быть натуральным числом.");
}