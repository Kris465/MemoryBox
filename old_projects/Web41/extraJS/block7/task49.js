const prompt = require('prompt-sync')();

const n = parseInt(prompt("Введите количество чисел (n):"), 10);
const a = [];

for (let i = 0; i < n; i++) {
    a.push(parseInt(prompt(`Введите число ${i + 1}:`), 10));
}

let firstIndex = -1;
let lastIndex = -1;

for (let i = 0; i < n; i++) {
    if (a[i] === 10) {
        if (firstIndex === -1) {
            firstIndex = i + 1; 
        }
        lastIndex = i + 1;
    }
}

if (firstIndex !== -1 && lastIndex !== -1) {
    console.log("Номер первого появления числа 10:", firstIndex);
    console.log("Номер последнего появления числа 10:", lastIndex);
} else {
    console.log("Число 10 в последовательности не встречается.");
}