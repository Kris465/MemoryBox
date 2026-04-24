const prompt = require('prompt-sync')();

const k = parseInt(prompt("Введите количество чисел:"));

const a = prompt(`Введите ${k} целых чисел через пробел:`).split(' ').map(Number);

let lastNegativeIndex = -1;

for (let i = 0; i < k; i++) {
    if (a[i] < 0) {
        lastNegativeIndex = i + 1; 
    }
}

console.log(lastNegativeIndex);