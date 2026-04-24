const prompt = require('prompt-sync')();

let a = prompt("Введите первое значение (a):");
let b = prompt("Введите второе значение (b):");


console.log("Перед обменом: ");
console.log("a = " + a);
console.log("b = " + b);


let temp = a; 
a = b;        
b = temp;    


console.log("После обмена: ");
console.log("a = " + a);
console.log("b = " + b);