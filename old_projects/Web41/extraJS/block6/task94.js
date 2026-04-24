const prompt = require('prompt-sync')(); 

const start = 200;
const divisor = 17;
const remainder = start % divisor;
const result = remainder === 0 ? start + divisor : start + (divisor - remainder);
console.log(result);