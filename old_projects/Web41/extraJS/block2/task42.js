const prompt = require('prompt-sync')();


let a = parseInt(prompt("Введите первое целое число (a): "));
let b = parseInt(prompt("Введите второе целое число (b): "));

console.log((a % b === 0 || b % a === 0) ? 1 : 0);