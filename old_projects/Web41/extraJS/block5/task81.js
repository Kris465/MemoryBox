const prompt = require('prompt-sync')();

function multiplyUsingLoop(x, y) {
    let result = 0;
    for (let i = 0; i < y; i++) {
        result += x;
    }
    return result;
}

const x1 = parseInt(prompt("Введите натуральное число x:"));
const y1 = parseInt(prompt("Введите натуральное число y:"));

if (x1 > 0 && y1 > 0) {
    const product1 = multiplyUsingLoop(x1, y1);
    console.log(`Произведение ${x1} и ${y1} (метод цикла): ${product1}`);
} else {
    console.log("Пожалуйста, введите корректные натуральные числа.");
}