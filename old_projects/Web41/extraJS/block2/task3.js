const prompt = require('prompt-sync')();

const massInKg = parseFloat(prompt("Введите массу в килограммах:"));
const tonn = Math.floor(massInKg / 1000);

console.log(`${tonn}`);