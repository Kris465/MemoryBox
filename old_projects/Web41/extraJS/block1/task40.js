const calc = (a, b) => {
    if (isNaN(a) || isNaN(b))
      return "Invalid input";
    if (a === 0)
      return "Division by zero";
    const x = (2 / (a * a + 25) + b) / (Math.sqrt(b) + (a + b) / 2),
      y = (Math.abs(a) + 2 * Math.sin(b)) / (5.5 * a);
    return { x, y };
  };
  const prompt = require('prompt-sync')();
  const a = parseFloat(prompt("a:")),
    b = parseFloat(prompt("b:"));
  const r = calc(a, b);
  console.log(typeof r === "string" ? r : `x=${r.x}, y=${r.y}`);