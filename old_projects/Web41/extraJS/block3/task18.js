function evaluateExpressions(X, Y) {
    const expressionA = !(X && !Y) || X; 
    const expressionB = (Y && !X) || !Y;
    const expressionC = (!Y && !X) || Y; 

    console.log(`X: ${X}, Y: ${Y}`);
    console.log(`а) не (X и не Y) или X: ${expressionA}`);
    console.log(`б) Y и не X или не Y: ${expressionB}`);
    console.log(`в) не Y и не X или Y: ${expressionC}`);
    console.log('-------------------');
}

console.log("Результаты для всех комбинаций X и Y:");
for (let X of [false, true]) {
    for (let Y of [false, true]) {
        evaluateExpressions(X, Y);
    }
}