const prompt = require('prompt-sync')(); 


const maxNumber = 5000;
const divisor = 39;
const result = maxNumber - (maxNumber % divisor);
console.log(result); // Выведет 4992