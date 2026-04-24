const prompt = require('prompt-sync')();

let a = parseInt(prompt('введите a:'));
let b = parseInt(prompt('введите b:'));
let c = parseInt(prompt('введите c:'));
let x = parseInt(prompt('введите x:'));
let R = parseInt(prompt('введите R:'));
let d = parseInt(prompt('введите d:'));

console.log(` а) a/b/c = ${a/b/c}`);
console.log(` б) (a * b)/c = ${(a*b)/c}`);
console.log(` в) (a/b) * c = ${(a/b) * c}`);
console.log(` г) a + (b/c) = ${a + (b/c)}`);
console.log(` д) (a + b) /c = ${(a+b) / c}`);
console.log(` е) (a + b)/(b + c)= ${(a+b)/(b+c)}`);
console.log(` ж) (a + b) / (b + c) = ${(a+b)/(b+c)}`); 
console.log(` з) a/sinb = ${a / (Math.sin(b * Math.PI/180))}`);
console.log(` и) 1/2 * a* b * sinx = ${1/2 * a * b * (Math.sin(x * Math.PI / 180))}`);
console.log(` к) (2 * b * c * cos) (a/2) / (b+c)= ${ (2 * b * c * (Math.cos(Math.PI / 180)))*(a/2) / (b+c)}`);
console.log(` л) (4 * R * sin)(a/2 * sin)(b/2 * sin) (c/2) = ${(4 * R * (Math.sin(Math.PI / 180)))*(a/2 * (Math.sin(Math.PI / 180)))*(b/2 * (Math.sin(Math.PI / 180))*(c/2))}`);
console.log(` м) (a * x + b) / (c * x +d) = ${(a*x+b)/(c*x+d)}`);
console.log(` н) (2 * sin ) (a + b) /2 * cos)(a - b) / 2= ${(2*Math.sin(Math.PI / 180))*(a+b) /2 * (Math.cos(Math.PI / 180))*(a-b)/2} `);
console.log(` о) abs(2 * sin ) * (-3 * abs(x/2))=${(Math.abs((Math.sin(2 * Math.PI / 180))))*(-3 * (Math.abs(x/2)))}`);
