function calculateExpressions() {
    const A = true;
    const B = false;
    const C = false;
  
    console.log(`A = ${A}, B = ${B}, C = ${C}`);
  
    const a = A || (B && !C);
    console.log(`  a) A || (B && !C): ${a}`);
  
    const b = !A && !B;
    console.log(`  b) !A && !B: ${b}`);
  
    const c = !(A && C) || B;
    console.log(`  c) !(A && C) || B: ${c}`);
  
    const d = A && !B || C;
    console.log(`  d) A && !B || C: ${d}`);
  
    const e = A && (!B || C);
    console.log(`  e) A && (!B || C): ${e}`);
  
    const f = A || ! (B && C);
    console.log(`  f) A || !(B && C): ${f}`);
  }
  
  calculateExpressions();
  
  