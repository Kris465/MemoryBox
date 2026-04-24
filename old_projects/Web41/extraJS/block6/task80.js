const prompt = require('prompt-sync')(); 

const numStr = prompt("Введите натуральное число:");
let count0 = 0;
let count9 = 0;

for (let digit of numStr) {
    if (digit === '0') count0++;
    if (digit === '9') count9++;
}

if (count0 > count9) {
    console.log("Цифра 0 встречается чаще.");
} else if (count9 > count0) {
    console.log("Цифра 9 встречается чаще.");
} else {
    console.log("Цифры 0 и 9 встречаются одинаковое количество раз.");
}