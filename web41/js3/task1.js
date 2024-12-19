const prompt = require('prompt-sync')();

let N = parseInt(prompt('Введите число N: '));
let result = [];

for (let i = 2; i <= N; i += 2) {
    result.push(i);
}

console.log(result.join(' '));
