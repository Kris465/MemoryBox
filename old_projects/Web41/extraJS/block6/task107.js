const prompt = require('prompt-sync')(); 


const m = parseInt(prompt("Введите число m:"), 10);
const n = parseInt(prompt("Введите число n:"), 10);
const max = Math.max(m, n);
const min = Math.min(m, n);
const result = [];
let i = min;

while (i <= max) {
    const isMultipleM = (i % m === 0) * i; 
    const isMultipleN = (i % n === 0) * i;
  
    result.push(isMultipleM * !!isMultipleM); 
    result.push(isMultipleN * !!isMultipleN);
    i++;
}

console.log(result.filter(x => x !== 0));