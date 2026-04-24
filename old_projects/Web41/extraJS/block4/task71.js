const prompt = require('prompt-sync')();

function findMaxMinSingle(a, b) {
    const max = (a > b) ? a : b; 
    const min = (a < b) ? a : b; 
    return { max, min };
}

const num1 = 7.8;
const num2 = 9.1;
const resultSingle = findMaxMinSingle(num1, num2);
console.log(`Наибольшее: ${resultSingle.max}, Наименьшее: ${resultSingle.min}`); 