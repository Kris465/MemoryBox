const prompt = require('prompt-sync')();

const sequence = [3.5, 7.2, 4.1, 9.0, 2.3]; 

let sum = 0;

for (let num of sequence) {
    const isOdd = Math.floor(num) % 2 !== 0;

    sum += isOdd * num;

    const continueLoop = !isOdd; 
    if (!continueLoop) break; 
}


console.log("Сумма подряд идущих в начале нечетных чисел:", sum);