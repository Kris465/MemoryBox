const prompt = require('prompt-sync')();
const n = 15; 

let count = 0;

for (let num = 100; num <= 999; num++) {
    const hundreds = Math.floor(num / 100);
    const tens = Math.floor((num % 100) / 10);
    const units = num % 10;

    if (hundreds + tens + units === n) {
        count++;
    }
}

console.log(`Количество трехзначных чисел, сумма цифр которых равна ${n}: ${count}`);