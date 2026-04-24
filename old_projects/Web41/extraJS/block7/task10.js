const prompt = require('prompt-sync')();
const n = 3; 

console.log(`Двухзначные числа, которые делятся на ${n} или содержат цифру ${n}:`);

for (let num = 10; num <= 99; num++) {
    const tens = Math.floor(num / 10);
    const units = num % 10;

    const divisibleByN = (num % n === 0);

    const containsN = (tens === n || units === n);

    if (divisibleByN || containsN) {
        console.log(num);
    }
}