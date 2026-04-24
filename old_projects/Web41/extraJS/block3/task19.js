function evaluateExpressions(A, B) {
    const expressionA = !(!A && !B) && A; 
    const expressionB = !(!A || !B) || A;
    const expressionC = !(!A || !B) && B; 

    console.log(`A: ${A}, B: ${B}`);
    console.log(`а) не (не A и не A) и A: ${expressionA}`);
    console.log(`б) не (не A или не B) или A: ${expressionB}`);
    console.log(`в) не (не A или не B) и B: ${expressionC}`);
    console.log('-------------------');
}

console.log("Результаты для всех комбинаций A и B:");
for (let X of [false, true]) {
    for (let Y of [false, true]) {
        evaluateExpressions(X, Y);
    }
}