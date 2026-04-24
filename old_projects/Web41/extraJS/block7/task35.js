
const prompt = require('prompt-sync')();
const n = parseInt(prompt("Введите натуральное число n:"), 10);
const a = [];

for (let i = 0; i < n; i++) {
    const num = parseInt(prompt(`Введите число a${i + 1}:`), 10);
    a.push(num);
}

let countEqualNeighbors = 0;
let countZeroNeighbors = 0;
let countEvenNeighbors = 0;
let countEnding5Neighbors = 0;

for (let i = 0; i < n - 1; i++) {
    if (a[i] === a[i + 1]) {
        countEqualNeighbors++;
    }
    if (a[i] === 0 || a[i + 1] === 0) {
        countZeroNeighbors++;
    }
    if (a[i] % 2 === 0 && a[i + 1] % 2 === 0) {
        countEvenNeighbors++;
    }
    if (
        a[i] % 10 === 5 || 
        a[i + 1] % 10 === 5 
    ) {
        countEnding5Neighbors++;
    }
}

console.log(`а) Количество пар равных соседних чисел: ${countEqualNeighbors}`);
console.log(`б) Количество пар, где хотя бы одно число равно нулю: ${countZeroNeighbors}`);
console.log(`в) Количество пар, где оба числа чётные: ${countEvenNeighbors}`);
console.log(`г) Количество пар, где хотя бы одно число заканчивается на цифру 5: ${countEnding5Neighbors}`);