function calculateExpressions() {
    const A = true;
    const B = false;
    const C = false;
  
    console.log(`A = ${A}, B = ${B}, C = ${C}`);
  
    const a = !A && B;
    console.log(`  a) !A && B: ${a}`);
  
    const b = A || !B;
    console.log(`  b) A || !B: ${b}`);
  
    const c = (A && B) || C;
    console.log(`  c) (A && B) || C: ${c}`);
  }
  
  calculateExpressions();