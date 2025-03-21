const prompt = require('prompt-sync')();

let number = parseInt(prompt('Введите число: '));
let divisors = [];

for (let i = 1; i <= number; i++) {
    if (number % i === 0) {
        divisors.push(i);
    }
}

console.log(`Делители числа ${number}: ${divisors.join(', ')}`);
