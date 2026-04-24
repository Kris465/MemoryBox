const prompt = require('prompt-sync')();
let a = prompt("введите длину ребра:");

let S = (6 * a * a);
let ob = (a * a * a);

console.log(`площадь полной поверхности куба: ${S}, объем: ${ob}`);