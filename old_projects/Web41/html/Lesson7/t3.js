function factorial(N) {
    let result = 1;
    for (let i = 1; i <= N; i++) {
        result *= i;
    }
    return result;
}

const prompt = require('prompt-sync')();
let num = Number(prompt("Введите число N: "));
console.log(factorial(num));