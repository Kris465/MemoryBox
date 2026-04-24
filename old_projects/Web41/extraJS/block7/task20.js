const prompt = require('prompt-sync')();

const nInput = prompt("Введите натуральное число n:");
const n = parseInt(nInput, 10);
const a = [];
for (let i = 1; i <= n; i++) {
    const input = prompt(`Введите число a${i}:`);
    const num = parseInt(input, 10);
    if (!isNaN(num)) {
        a.push(num);
    } else {
        console.log("Некорректный ввод");
        i--;
    }
}
console.log("а) все элементы:", a.join(' '));
console.log("б) первый и последний элементы:", a[0], a[n - 1]);
console.log("в) первый и второй элементы:", a[0], a[1]);