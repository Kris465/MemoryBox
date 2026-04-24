const prompt = require('prompt-sync')();

function gcd(a, b) {

    if (b === 0) {
        return a;
    }

    return gcd(b, a % b);
}


const num1 = prompt("Введите число: ");
const num2 = prompt("Введите число: ");
console.log(`Наибольший общий делитель ${num1} и ${num2} равен ${gcd(num1, num2)}`);