const prompt = require('prompt-sync')();

let a = parseInt(prompt('Введите первое число: '));
let b = parseInt(prompt('Введите второе число: '));

while (b !== 0) {
    let temp = b;
    b = a % b;
    a = temp;
}

console.log(`Наибольший общий делитель: ${a}`);
