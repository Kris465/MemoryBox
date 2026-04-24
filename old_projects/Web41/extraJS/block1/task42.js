const calc = (e, f, g, h) => {
    if (isNaN(e) || isNaN(f) || isNaN(g) || isNaN(h))
      return "Invalid input";
    const a = e + f / 2 / 3
    b = Math.abs(Math.pow(h, 2) - g)
    if (e * 2 * 3 / f === 0)
        return "Division by zero";
    const c = Math.sqrt(Math.pow(g - h, 2) - 3 * Math.sin(e))
    return { a, b, c };
};
const prompt = require("prompt-sync")();
const e = parseFloat(prompt("e:")),
  f = parseFloat(prompt("f:")),
  g = parseFloat(prompt("g:")),
  h = parseFloat(prompt("h:"));
const r = calc(e, f, g, h);
  
console.log(typeof r === "string" ? r : `a=${Math.round(r.a, 2)}, b=${Math.round(r.b, 2)}, c=${Math.round(r.c, 2)}`);