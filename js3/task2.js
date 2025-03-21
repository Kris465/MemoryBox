const prompt = require('prompt-sync')();

let N = parseInt(prompt('Введите число N: '));
let result = [];

if (N % 2 === 0) {
    N -= 1;
}

for (let i = N; i >= 1; i -= 2) {
    result.push(i);
}

console.log(result.join(' '));
