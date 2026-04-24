const prompt = require('prompt-sync')();

const b = [];
for (let i = 0; i < 8; i++) {
    b.push(parseFloat(prompt(`Введите число b${i + 1}:`)));
}
let countLessThan100 = 0;
for (let i = 0; i < 8; i++) {
    if (b[i] < 100) {
        countLessThan100++;
    }
}
console.log("Количество чисел меньше 100:", countLessThan100);