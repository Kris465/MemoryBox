function evaluateExpressions(A, B) {
    const notAAndNotBOrA = (!A && !B) || A; 
    const BOrNotAAndNotB = B || (!A && !B); 
    const BAndNotAAndNotB = B && !(A && !B); 

    console.log(`A: ${A}, B: ${B}`);
    console.log(`а) не A и не B или A: ${notAAndNotBOrA}`);
    console.log(`б) B или не A и не B: ${BOrNotAAndNotB}`);
    console.log(`в) B и не (A и не B): ${BAndNotAAndNotB}`);
    console.log('-------------------');
}


console.log("Результаты для всех комбинаций A и B:");
for (let A of [false, true]) {
    for (let B of [false, true]) {
        evaluateExpressions(A, B);
    }
}