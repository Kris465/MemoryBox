const prompt = require('prompt-sync')(); 

const sequence = [1, 1, 2, 1, 2, 3, 0]; 


function getCumulativeSum(arr) {
    const result = [];
    let sum = 0;
    for (let num of arr) {
        if (num === 0) break; 
        sum += num;
        result.push(sum);
    }
    return result;
}

const cumulativeSequence = getCumulativeSum(sequence);
console.log(cumulativeSequence.join(' '));