const prompt = require('prompt-sync')(); 

const n = 50;

function printSquaresUpToN(n) {
    let i = 1;
    while (i * i <= n) {
        console.log(i * i);
        i++;
    }
}

printSquaresUpToN(n);