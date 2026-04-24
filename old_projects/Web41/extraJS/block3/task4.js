function calculateExpressions() {
    const X = true;
    const Y = true;
    const Z = false;

    console.log(`X = ${X}, Y = ${Y}, Z = ${Z}`);

    const a = !X && Y;
    console.log(`  a) !X && Y: ${a}`);

    const b = X || !Y;
    console.log(`  b) X || !Y: ${b}`);

    const c = X || (Y && Z);
    console.log(`  c) X || (Y && Z): ${c}`);
}

calculateExpressions();