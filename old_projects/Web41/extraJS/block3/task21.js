function evaluateExpressions(A, B, C) {

    const expressionA = !(A || (!B && C)); 
    const expressionB = A && !(B || !C);   
    const expressionC = !(!A || (B && C));
    console.log(`A: ${A}, B: ${B}, C: ${C}`);
    console.log(`а) не (A или не B и C): ${expressionA}`);
    console.log(`б) A и не (B или не C): ${expressionB}`);
    console.log(`в) не (не A или B и C): ${expressionC}`);
    console.log('-------------------');
}

console.log("Результаты для всех комбинаций A, B и C:");
for (let A = 0; A <= 1; A++) {
    for (let B = 0; B <= 1; B++) {
        for (let C = 0; C <= 1; C++) {
            evaluateExpressions(Boolean(A), Boolean(B), Boolean(C));
        }
    }
}