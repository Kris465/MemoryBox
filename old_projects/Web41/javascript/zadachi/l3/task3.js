const prompt = require('prompt-sync')();
let num = prompt("Введите число :");
for (let i = 1; i < num; i += 1) {
    if (num % i == 0) {
        console.log(i)
    }
  
    
}