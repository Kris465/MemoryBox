const prompt = require('prompt-sync')();

let N = parseInt(prompt('Введите число N: '));
let result = [];

for (let i = 1; i <= N; i++) {
    if (N % i === 0) {
        result.push(i);
    }
}

console.log(result.join(', '));
