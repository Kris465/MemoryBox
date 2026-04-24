const prompt = require('prompt-sync')();

const m = parseInt(prompt("Введите количество чисел (m):"), 10);
const x = [];

for (let i = 0; i < m; i++) {
    const num = parseInt(prompt(`Введите число x${i + 1}:`), 10);
    x.push(num);
}

let countDivBy3 = 0;
let countDivBy7 = 0;

for (let i = 0; i < m; i++) {
    if (x[i] % 3 === 0) {
        countDivBy3++;
    }
    if (x[i] % 7 === 0) {
        countDivBy7++;
    }
}

console.log(`Количество чисел, кратных 3: ${countDivBy3}`);
console.log(`Количество чисел, кратных 7: ${countDivBy7}`);