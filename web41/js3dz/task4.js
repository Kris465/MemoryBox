const prompt = require('prompt-sync')();

let number = parseInt(prompt('Введите число: '));
let count = 0;

while (number !== 0) {
    number = Math.floor(number / 10);
    count++;
}

console.log(`Количество цифр: ${count}`);
