function calculateExpressions() {
    const X = false;
    const Y = true;
    const Z = false;
  
    console.log(`X = ${X}, Y = ${Y}, Z = ${Z}`);
  
    const a = X || Z;
    console.log(`  a) X || Z: ${a}`);
  
    const b = X && Y;
    console.log(`  b) X && Y: ${b}`);
  
    const c = X && Z;
    console.log(`  c) X && Z: ${c}`);
  }
  
  calculateExpressions();