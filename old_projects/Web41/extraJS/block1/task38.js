const prompt = require('prompt-sync')();

function trapPerimeter(a, b, h) {
    const side = Math.sqrt(((a - b) / 2) ** 2 + h ** 2);
    return (a + b )/2 * side;
  }
  const a = Number(prompt("Основание a: "));
  const b = Number(prompt("Основание b: "));
  const h = Number(prompt("Высота h: "));
  
  console.log("Периметр:", trapPerimeter(a, b, h));