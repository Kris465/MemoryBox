const prompt = require('prompt-sync')();

function calculateSum(n) {
    let sum = 0;


    for (let i = 0; i < n; i++) {
        sum += 1;
    }

 
    for (let j = 1; j <= n; j++) {
        sum += j;
    }

    return sum;
}


let n = parseInt(prompt("Введите натуральное число n:"));
if (n > 0) {
    let result = calculateSum(n);
    console.log("Сумма:", result);
} else {
    console.log("Ошибка: n должно быть натуральным числом.");
}