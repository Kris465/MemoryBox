const calc = (e, f, g, h) => {
    if (isNaN(e) || isNaN(f) || isNaN(g) || isNaN(h))
      return "Invalid input";
    const a = Math.sqrt(Math.abs(e - 3 / f) ** 3) + g,
      b = Math.sin(e) + Math.cos(h) ** 2;
    if (e * f - 3 === 0)
      return "Division by zero";
    const c = 33 * g / (e * f - 3);
    return { a, b, c };
  };
  const prompt = require("prompt-sync")();
  const e = parseFloat(prompt("e:")),
    f = parseFloat(prompt("f:")),
    g = parseFloat(prompt("g:")),
    h = parseFloat(prompt("h:"));
  const r = calc(e, f, g, h);
  
  console.log(typeof r === "string" ? r : `a=${Math.round(r.a, 2)}, b=${Math.round(r.b, 2)}, c=${Math.round(r.c, 2)}`);