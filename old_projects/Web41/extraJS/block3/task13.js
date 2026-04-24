const values = [true, false];

function evaluateExpressions(A, B) {
    const notAnd = !(A && B);
    const notAOrB = !A || B;   
    const AOrNotB = A || !B;   

    console.log(`A: ${A}, B: ${B}`);
    console.log(`а) не (A и B): ${notAnd}`);
    console.log(`б) не A или B: ${notAOrB}`);
    console.log(`в) A или не B: ${AOrNotB}`);
    console.log('-------------------');
}

for (let A of values) {
    for (let B of values) {
        evaluateExpressions(A, B);
    }
}