const prompt = require('prompt-sync')();

function per(a, b) {
    return (a+b+(Math.sqrt(a ^ 2 + b ^ 2)));
}
  
const cathetusA = Number(prompt("Введите длину первого катета: "));
const cathetusB = Number(prompt("Введите длину второго катета: "));
  
const hypotenuse = per(cathetusA, cathetusB);
  
console.log("Периметр:", hypotenuse);