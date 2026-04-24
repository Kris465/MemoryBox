function evaluateExpressions(A, B, C) {

    const expressionA = !(A && B) && (!A || !C); 
    const expressionB = !(A && !B) || (A || !C); 
    const expressionC = (A && !B) || !(A || !C); 


    console.log(`A: ${A}, B: ${B}, C: ${C}`);
    console.log(`а) не (А и В) и (не А или не С): ${expressionA}`);
    console.log(`б) не (А и не В) или (А или не С): ${expressionB}`);
    console.log(`в) А и не В или не (А или не С): ${expressionC}`);
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