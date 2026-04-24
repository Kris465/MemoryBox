const prompt = require('prompt-sync')();

let a = prompt("Введите первое значение (a): ");
let b = prompt("Введите второе значение (b): ");
let c = prompt("введите третье значение(c): ");

console.log("Исходные значения:");
console.log("a =", a, "b =", b, "c =", c);

let tempA = a;
a = b;
b = c;
c = tempA; 

console.log("После первой замены:");
console.log("a =", a, "b =", b, "c =", c);

a = 1;
b = 2;
c = 3;


console.log("Исходные значения для второй замены:");
console.log("a =", a, "b =", b, "c =", c);


let tempB = b; 
b = a;
a = c; 
c = tempB; 

console.log("После второй замены:");
console.log("a =", a, "b =", b, "c =", c);
