const prompt = require('prompt-sync')();

function findMaxMin(a, b, c) {
    const max = (a > b) ? ((a > c) ? a : c) : ((b > c) ? b : c);
    
    const min = (a < b) ? ((a < c) ? a : c) : ((b < c) ? b : c);

    return { max, min };
}

const a = 5.5; 
const b = 3.2;
const c = 7.8;

const result = findMaxMin(a, b, c);
console.log("Максимальное значение:", result.max);
console.log("Минимальное значение:", result.min);