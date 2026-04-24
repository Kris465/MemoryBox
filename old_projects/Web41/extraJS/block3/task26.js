function evaluateExpressions(X, Y, Z) {

    const expressionA = !(X || Y) && (!X || !Z); 
    const expressionB = !(!X && Y) || (X && !Z); 
    const expressionC = X || !Y && !(X || !Z); 


    console.log(`X: ${X}, Y: ${Y}, Z: ${Z}`);
    console.log(`а) не (X или Y) и (не X или не Z): ${expressionA}`);
    console.log(`б) не (не X и Y) или (X и не Z): ${expressionB}`);
    console.log(`в) X или не Y и не (X или не Z): ${expressionC}`);
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