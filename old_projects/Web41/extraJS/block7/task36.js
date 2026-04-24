const prompt = require('prompt-sync')();


const n = parseInt(prompt("Введите натуральное число n:"), 10);
const x = [];

for (let i = 0; i < n; i++) {
    const num = parseFloat(prompt(`Введите вещественное число x${i + 1}:`));
    x.push(num);
}

let countGreaterThanNeighbors = 0;

for (let i = 1; i < n - 1; i++) {
    if (x[i] > x[i - 1] && x[i] > x[i + 1]) {
        countGreaterThanNeighbors++;
    }
}


console.log(`Количество чисел, больших своих соседей: ${countGreaterThanNeighbors}`);