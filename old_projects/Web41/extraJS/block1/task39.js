function calc(x, y) {
    const d = y + 1 / Math.sqrt(x * x + 10);
    if (d === 0) return "Zero division";
    const z = (x + (2 + y) / (x * x)) / d;
    const q = 2.8 * Math.sin(x) + Math.abs(y);
    return { z, q };
  }
  
const prompt = require('prompt-sync')();
const x = parseFloat(prompt("x:"));
const y = parseFloat(prompt("y:"));
const r = calc(x, y);
console.log(typeof r === 'string' ? r : `z=${r.z} q=${r.q}`);