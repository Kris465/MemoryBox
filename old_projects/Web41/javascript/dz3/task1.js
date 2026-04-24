const prompt = require('prompt-sync')();
let num1 = Number(prompt("Введите первое число: "));
let num2 = Number(prompt("Введите второе число: "));
let summa = 0;

for (let i = num1; i <= num2; i ++){
    summa += i;
}

console.log(`сумма равна ${summa}`);


