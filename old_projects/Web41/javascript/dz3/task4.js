const prompt = require('prompt-sync')();
let num1 = Number(prompt("Введите число: "));
let i = 0;

while (num1 != 0 ) {
    num1 = Math.floor(num1 / 10);
    i ++;

}
console.log(`цифр в числе ${i}`);