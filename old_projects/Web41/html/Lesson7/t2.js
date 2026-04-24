function sumToN(N) {
    let sum = 0;
    for (let i = 1; i <= N; i++ ){
        sum += i;
    }
    return sum;
}

const prompt = require('prompt-sync')();
let num = Number(prompt("Введите число N: "));
console.log(sumToN(num));