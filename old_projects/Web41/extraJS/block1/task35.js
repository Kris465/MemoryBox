const prompt = require('prompt-sync')();

function svinota(a, b) {
    return Math.sqrt(a * a + b * b);
  }
  

  
  const cathetusA = prompt("Введите длину первого катета: ");
  const cathetusB = prompt("Введите длину второго катета: ");
  
  const hypotenuse = svinota(cathetusA, cathetusB);
  
  console.log("Гипотенуза:", hypotenuse);