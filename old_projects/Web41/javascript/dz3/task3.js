const prompt = require('prompt-sync')();
let num1 = Number(prompt("Введите число: "));
let div = [];

for (let i = 2; i <= num1; i ++) {
    if (num1 % i == 0){
        div.push(i);
    }
}
console.log(`делители числа ${num1} это ${div}`);