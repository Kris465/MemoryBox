const prompt = require('prompt-sync')();

const c = [];
for (let i = 1; i <= 15; i++) {
    const input = prompt(`Введите число c${i}:`);
    const num = parseFloat(input);
    if (!isNaN(num)) {
        c.push(num);
    } else {
        console.log("Некорректный ввод");
        i--;
    }
}
let result = c[0];
for (let i = 2; i < 15; i += 2) {
    result -= c[i];
}
console.log(result);