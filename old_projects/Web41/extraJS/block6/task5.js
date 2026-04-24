const prompt = require('prompt-sync')();

const n = parseInt(prompt("Введите длину последовательности:"), 10);
const sequence = [];
for (let i = 0; i < n; i++) {
    sequence.push(parseInt(prompt(`Введите число ${i + 1}:`), 10));
}

const firstElement = sequence[0];
let count = 0;

for (let num of sequence) {
    const isEqual = num === firstElement;
    count += isEqual * 1;
    const continueLoop = !isEqual;
    if (!continueLoop) break;
}

console.log("Количество одинаковых элементов в начале последовательности:", count);