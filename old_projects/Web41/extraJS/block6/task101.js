const prompt = require('prompt-sync')(); 

function gcd(a, b) {
    while (b !== 0) {
        const temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

const num1 = prompt("введите первое число: ");
const num2 = prompt("введите второе число: ");

console.log(`Наибольший общий делитель ${num1} и ${num2} равен ${gcd(num1, num2)}`);