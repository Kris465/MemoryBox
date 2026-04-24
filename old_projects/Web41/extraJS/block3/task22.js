function evaluateExpressions(X, Y, Z) {
   
    const expressionA = !(X || (!Y && Z)); 
    const expressionB = Y || (X && !Y || Z); 
    const expressionC = !(!X && Y || Z);

  
    console.log(`X: ${X}, Y: ${Y}, Z: ${Z}`);
    console.log(`а) не (X или не Y и Z): ${expressionA}`);
    console.log(`б) Y или (X и не Y или Z): ${expressionB}`);
    console.log(`в) не (не X и Y или Z): ${expressionC}`);
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