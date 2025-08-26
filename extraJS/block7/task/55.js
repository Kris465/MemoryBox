const prompt = require('prompt-sync')();

const n = parseInt(prompt("Введите количество элементов n:"), 10);
const a = [];
for (let i = 0; i < n; i++) {
    a.push(parseInt(prompt(`Введите элемент a[${i + 1}]:`), 10));
}

let maxVal = a[0];
let minVal = a[0];
let maxIndex = 0;
let minIndex = 0;

for (let i = 1; i < n; i++) {
    if (a[i] >= maxVal) {
        maxVal = a[i];
        maxIndex = i;
    }
    if (a[i] <= minVal) {
        minVal = a[i];
        minIndex = i;
    }
}

console.log(`Номер последнего максимального элемента: ${maxIndex + 1}`);
console.log(`Номер последнего минимального элемента: ${minIndex + 1}`);