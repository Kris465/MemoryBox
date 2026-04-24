const prompt = require('prompt-sync')();
let x = prompt("введите значение х:");
let y = prompt("введите значение y:");
let a = prompt("введите значение a:");
let b = prompt("введите значение b:");

let c = (z = Math.pow(x, 3) - 2.5 * x * y + 1.78 * Math.pow(x, 2) - 2.5 * y + 1);
let d = (x = 3.56 * a + Math.pow(b, 3) - 5.8 * Math.pow(b, 2) + 3.8 * a - 1.5);
console.log(`Ответ: ${c} и ${d}`);