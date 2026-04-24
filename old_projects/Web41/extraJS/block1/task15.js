const prompt = require('prompt-sync')();

let x = parseInt(prompt('введите x:'));
let a = parseInt(prompt('введите a:'));
let b = parseInt(prompt('введите b:'));
let c = parseInt(prompt('введите c:'));
let m = parseInt(prompt('введите м:'));
let n = parseInt(prompt('введите n:'));

console.log(` а) -1 / (x * x) = ${-1 / (x * x)}`);
console.log(` б) a / (b * c) = ${a / (b * c)} `);
console.log(` в) (a / b) * c = ${(a / b) * c}`);
console.log(` г) (a + b) / 2 = ${(a + b) / 2}`);
console.log(` д)  5,45 * (a + 2b) / 2 - a = ${5,45 * (a + 2 * b) / 2 - a}`);
console.log(` е) -b + sqrt(b Math.sqrt(2) - 4ac) / 2a = ${-b + Math.sqrt(b = Math.sqrt(2) - 4 * a * c ) / (2 * a) } `);
console.log(` ж) -b + 1 / a / 2 / c = ${-b + (1 / a ) / (2 / c)}`);
console.log(` з) 1 / 1 + a + b / 2 = ${1 / 1 + (a + b) / 2}`);
console.log(` и) 1 / 1 + 1 / 2 + 1 / 2 + 3 / 5 = ${1 / (1 + 1 / 2 + 1 / 2 + 3 / 5)} `);
console.log(` к) 2 * (m * n) = ${Math.pow(2, m * n)}`); 