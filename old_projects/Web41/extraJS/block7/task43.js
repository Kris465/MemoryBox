const prompt = require('prompt-sync')();

const numbers = [];
for (let i = 0; i < 9; i++) {
    const input = prompt(`Введите число ${i + 1} из 9:`);
    const num = parseFloat(input);
    numbers.push(num);
}

let sum = 0;
let count = 0;

for (let num of numbers) {
    if (num > 10) {
        sum += num;
        count++;
    }
}

const average = sum / count;

console.log(`Среднее арифметическое чисел больше 10: ${average}`);
