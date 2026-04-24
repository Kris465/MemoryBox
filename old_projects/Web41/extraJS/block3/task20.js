function evaluateExpressions(X, Y) {
    const expressionA = !(!X || Y) || !X;
    const expressionB = !(!X && !Y) && X; 
    const expressionC = !(X || !Y) || !Y;

    console.log(`X: ${X}, Y: ${Y}`);
    console.log(`а) не (не X или Y) или не X: ${expressionA}`);
    console.log(`б) не (не X и не Y) и X: ${expressionB}`);
    console.log(`в) не (X или не Y) или не Y: ${expressionC}`);
    console.log('-------------------');
}

console.log("Результаты для всех комбинаций X и Y:");
for (let X of [false, true]) {
    for (let Y of [false, true]) {
        evaluateExpressions(X, Y);
    }
}