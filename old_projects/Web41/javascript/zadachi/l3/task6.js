const prompt = require('prompt-sync')();
let num = prompt('введите первоначальный обьем воды: ');
let days = 0;
while (num >= 10) {
    num *= 0.9;
    days ++;
}
console.log(days);