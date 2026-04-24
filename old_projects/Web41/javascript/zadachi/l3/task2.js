const prompt = require('prompt-sync')();
let num = prompt("Введите число :");
for (let i = num; i >= 1; i -= 2) {
    console.log(i)
}