const prompt = require('prompt-sync')(); 

const n = 20; 

function findFirstSquareGreaterThanN(n) {
    let i = 1;
    while (true) {
        const square = i * i;
        if (square > n) {
            return square;
        }
        i++;
    }
}

const result = findFirstSquareGreaterThanN(n);
console.log(`Первое число из последовательности, большее ${n}: ${result}`);