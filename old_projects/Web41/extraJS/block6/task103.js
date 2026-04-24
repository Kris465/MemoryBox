const prompt = require('prompt-sync')(); 

function gcd(a, b) {
    while (b !== 0) {
        const temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

const a = parseInt(prompt("Введите числитель дроби:"), 10);
const b = parseInt(prompt("Введите знаменатель дроби:"), 10);

if (isNaN(a) || isNaN(b) || a <= 0 || b <= 0) {
    console.log("Пожалуйста, введите натуральные числа больше нуля.");
} else {
    const divisor = gcd(a, b);
    const p = a / divisor;
    const q = b / divisor;
    console.log(`Сокращённая дробь: ${p}/${q}`);
}