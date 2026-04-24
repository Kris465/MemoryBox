const prompt = require('prompt-sync')();


const n = parseInt(prompt("Введите количество чисел:"));

const input = prompt(`Введите ${n} целых чисел через пробел:`).split(' ').map(Number);

let lastIndex = -1;

for (let i = 0; i < n; i++) {
    if (input[i] > 100) {
        lastIndex = i + 1; 
    }
}


console.log(lastIndex);