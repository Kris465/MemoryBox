const prompt = require('prompt-sync')(); 

function gcd(a, b) {
    while (b !== 0) {
        const temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

function lcm(a, b) {
    return (a * b) / gcd(a, b);
}

const num1 = parseInt(prompt("Введите первое натуральное число:"), 10);
const num2 = parseInt(prompt("Введите второе натуральное число:"), 10);

if (isNaN(num1) || isNaN(num2) || num1 <= 0 || num2 <= 0) {
    console.log("Пожалуйста, введите натуральные числа больше нуля.");
} else {
    const result = lcm(num1, num2);
    console.log(`Наименьшее общее кратное ${num1} и ${num2} равно ${result}.`);
}






