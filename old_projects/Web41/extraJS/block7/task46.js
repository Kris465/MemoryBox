const prompt = require('prompt-sync')();

const m = parseInt(prompt("Введите количество чисел (m):"), 10);
const n = parseInt(prompt("Введите число n:"), 10);
const a = [];

for (let i = 0; i < m; i++) {
    a.push(parseInt(prompt(`Введите число ${i + 1}:`), 10));
}

const multiplesOfN = a.filter(num => num % n === 0);
const sumMultiples = multiplesOfN.reduce((sum, num) => sum + num, 0);
const average = sumMultiples / multiplesOfN.length;

console.log("Среднее арифметическое чисел, кратных", n, ":", average);