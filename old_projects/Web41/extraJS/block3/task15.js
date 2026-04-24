
const values = [true, false];

function evaluateExpressions(A, B) {
    const notAOrNotB = !A || !B; 
    const AAndAOrNotB = A && (A || !B); 
    const notAOrBAndB = (!A || B) && B; 
    console.log(`A: ${A}, B: ${B}`);
    console.log(`а) не A или не B: ${notAOrNotB}`);
    console.log(`б) A и (A или не B): ${AAndAOrNotB}`);
    console.log(`в) (не A или B) и B: ${notAOrBAndB}`);
    console.log('-------------------');
}

for (let A of values) {
    for (let B of values) {
        evaluateExpressions(A, B);
    }
}