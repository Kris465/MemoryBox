
function evaluateExpressions(X, Y, Z) {

    const expressionA = !(Y || (!X && Z)) || Z; 
    const expressionB = X && !( !Y || Z) || Y;
    const expressionC = !(X || (Y && Z)) || !X; 


    console.log(`X: ${X}, Y: ${Y}, Z: ${Z}`);
    console.log(`а) не (Y или не X и Z) или Z: ${expressionA}`);
    console.log(`б) X и не (не Y или Z) или Y: ${expressionB}`);
    console.log(`в) не (X или Y и Z) или не X: ${expressionC}`);
    console.log('-------------------');
}

console.log("Результаты для всех комбинаций X, Y и Z:");
for (let X = 0; X <= 1; X++) {
    for (let Y = 0; Y <= 1; Y++) {
        for (let Z = 0; Z <= 1; Z++) {
            evaluateExpressions(Boolean(X), Boolean(Y), Boolean(Z));
        }
    }
}