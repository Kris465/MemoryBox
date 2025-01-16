const prompt = require('prompt-sync')(); 

let x = prompt('введите значение x ')
let a = prompt('введите значение a ')
let y = prompt('введите значение y ')
let n = prompt('введите значение n ')
let aResult = 2*x;
let bResult = Math.sin(x * Math.PI / 180);
let cResult = Math.pow(a, 2);
let dResult = Math.sqrt(x);
let eResult = Math.abs(n);
let fResult = 5*Math.cos(y);
let gResult = -7.5*Math.pow(a, 2);
let hResult = 3*Math.sqrt(x);

console.log(`a) 2x = ${aResult}`);
console.log(`b) sin x = ${bResult}`);
console.log(`c) a² = ${cResult}`);
console.log(`d) √x = ${dResult}`);
console.log(`e) |n| = ${eResult}`);
console.log(`f) 5cos y = ${fResult}`);
console.log(`g) -7.5a² = ${gResult}`);
console.log(`h) 3√x = ${hResult}`);