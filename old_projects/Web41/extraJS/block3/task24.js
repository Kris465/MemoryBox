
function evaluateExpressions(A, B, C) {
    const expressionA = !(A || (!B && C)) || C; 
    const expressionB = !(A && !B || C) && B; 
    const expressionC = !(!A || (B && C)) || A; 

    console.log(`A: ${A}, B: ${B}, C: ${C}`);
    console.log(`а) не (A или не B и C) или C: ${expressionA}`);
    console.log(`б) не (A и не B или C) и B: ${expressionB}`);
    console.log(`в) не (не A или B и C) или A: ${expressionC}`);
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