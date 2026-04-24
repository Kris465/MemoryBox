const prompt = require('prompt-sync')();

const a = [];
for (let i = 1; i <= 20; i++) {
    const input = prompt(`Введите число a${i}:`);
    const num = parseInt(input, 10);
    if (!isNaN(num)) {
        a.push(num);
    } else {
        console.log("Некорректный ввод");
        i--;
    }
}
let sum = 0;
for (let i = 1; i <= 19; i += 2) {
    sum += a[i];
}
console.log(sum);