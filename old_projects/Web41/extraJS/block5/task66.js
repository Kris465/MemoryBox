const prompt = require('prompt-sync')();

function generateSequence(n) {
    const sequence = [];
    for (let i = 1; i <= n; i++) {
        sequence.push(i);
    }
    return sequence;
}

const n = 10; 
const result = generateSequence(n);
console.log(result);