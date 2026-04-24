const prompt = require('prompt-sync')();

const sequence = [3, -1, 4, 0]; 
let sum = 0;
let count = 0;

for (let num of sequence) {
    if (num === 0) break; 
    sum += num;
    count++;
}

console.log("Сумма всех чисел:", sum);
console.log("Количество чисел:", count);